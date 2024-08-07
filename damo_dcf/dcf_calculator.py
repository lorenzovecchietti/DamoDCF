from typing import Optional, Tuple

import numpy as np
import pandas as pd
import toml
from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from damo_dcf.option_calculator import OptionData

# import src.compdata.comp_data as damo_data


class StockData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    revenue: int
    operating_income: int
    interest_expense: int
    book_value_of_equity: int
    book_value_of_debt: int
    cash_and_marketable_securities: int
    cross_holdings_and_other_non_operating_assets: int = 0
    minority_interests: int = 0
    number_of_shares_outstanding: int
    carryforward_nol: float = 0.0
    effective_tax_rate: float
    annualized_dividend: float


class MarketData(BaseModel):
    riskfree_rate: float
    marginal_tax_rate: float


class DCFAssumptions(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    revenue_growth: np.ndarray | float
    operating_margin: np.ndarray | float
    sales_to_capital_ratio: np.ndarray | float
    tax_rate: np.ndarray | float
    cost_of_capital: np.ndarray | float
    return_on_capital: Optional[float] = None

    def _get_all_arrays(self):
        return [
            self.__getattribute__(field)
            for field in [
                "revenue_growth",
                "operating_margin",
                "sales_to_capital_ratio",
                "tax_rate",
                "cost_of_capital",
            ]
        ]

    @field_validator(
        "revenue_growth",
        "operating_margin",
        "sales_to_capital_ratio",
        "tax_rate",
        "cost_of_capital",
        mode="before",
    )
    def make_ndarray(cls, v):
        if isinstance(v, list):
            v = np.asarray(v)
        return v

    @model_validator(mode="after")
    def check_equal_length(self) -> "DCFAssumptions":
        arrays = self._get_all_arrays()
        if (
            len(
                {
                    len(array)
                    for array in arrays
                    if array is not None and isinstance(array, np.ndarray)
                }
            )
            > 1
        ):
            raise ValueError("All arrays must have the same length.")
        return self

    @model_validator(mode="after")
    def check_all_same_types(self) -> "DCFAssumptions":
        arrays = self._get_all_arrays()
        if not all(isinstance(array, np.ndarray) for array in arrays) and not all(
            isinstance(array, float) for array in arrays
        ):
            raise ValueError("All fields must be either a numpy array or float")
        return self


class DCFCalculator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    ticker_symbol: str
    multiplier: int
    stock_data: StockData
    current_stock_price: float
    dcf_assumptions: DCFAssumptions
    dcf_terminal: DCFAssumptions
    market_data: MarketData
    option_data: Optional[OptionData] = None
    _future_financials: Optional[pd.DataFrame] = None
    _equity_value: Optional[float] = None

    def __init__(self, input_toml: str):
        with open(input_toml, "r") as file:
            data = toml.load(file)
        financials = {k: v * data["multiplier"] for k, v in data["firm_data"].items()}
        if data.get("options", False):
            data["options"]["ticker_symbol"] = data["ticker_symbol"]
            data["options"]["n_o"] = int(data["multiplier"] * data["options"]["n_o"])
            option_data = OptionData(**data["options"])
        else:

            option_data = None
        super().__init__(
            ticker_symbol=data["ticker_symbol"],
            multiplier=data["multiplier"],
            current_stock_price=data["current_stock_price"],
            stock_data=StockData(**financials),
            dcf_assumptions=DCFAssumptions(**data["future_assumptions"]),
            dcf_terminal=DCFAssumptions(**data["terminal_values"]),
            market_data=MarketData(**data["market_data"]),
            option_data=option_data,
        )

    @property
    def future_financials(self):
        if self._future_financials is None:
            self._compute_future_financials()
        return self._future_financials

    @property
    def _years_to_predict(self) -> int:
        return self.dcf_assumptions.revenue_growth.size + 2

    @property
    def stock_value(self) -> float:
        return self.equity_value / self.stock_data.number_of_shares_outstanding

    @property
    def equity_value(self) -> float:
        if self._equity_value is None:
            equity_value = self._run_dcf()
        else:
            equity_value = self._equity_value
        return equity_value

    def update(self):
        self._future_finantials = None
        self._equity_value = None
        self.run_dcf()

    def run_dcf(self):
        cum_disc_factor, pv = self._discount_cash_flows(
            self.future_financials["FCFF"].values[1:-1]
        )
        terminal_cash_flow = (
            self.future_financials["FCFF"].values[-1]
            / (self.dcf_terminal.cost_of_capital - self.dcf_terminal.revenue_growth)
            * cum_disc_factor
        )
        equity_value = (
            pv
            + terminal_cash_flow
            - self.stock_data.book_value_of_debt
            + -self.stock_data.minority_interests
            + self.stock_data.cash_and_marketable_securities
            + self.stock_data.cross_holdings_and_other_non_operating_assets
        )  # TODO: add failure
        if self.option_data is not None:
            equity_value -= self.option_data.black_scholes_call(
                self.current_stock_price,
                self.stock_data.annualized_dividend,
                self.market_data.riskfree_rate,
                self.stock_data.number_of_shares_outstanding,
            )

        self._equity_value = equity_value

    def _discount_cash_flows(self, cash_flows: np.ndarray) -> Tuple[float, float]:
        discounted_factor = 1 / (1 + self.dcf_assumptions.cost_of_capital)
        cumulative_discounted_factor = np.cumprod(discounted_factor)
        return cumulative_discounted_factor[-1], np.sum(
            cumulative_discounted_factor * cash_flows
        )

    def _compute_future_financials(self):
        years = self._years_to_predict
        # Creazione array per gli anni
        revenues = np.zeros(years)
        ebit_income = np.zeros(years)
        tax_rate = np.zeros(years)
        margin = np.zeros(years)
        reinvestment = np.zeros(years)
        fcff = np.zeros(years)
        nol = np.zeros(years)
        net_income = np.zeros(years)

        # Valori iniziali
        revenues[0] = self.stock_data.revenue
        ebit_income[0] = self.stock_data.operating_income
        margin[0] = ebit_income[0] / revenues[0]
        tax_rate[0] = self.stock_data.effective_tax_rate
        reinvestment[0] = None
        fcff[0] = None
        nol[0] = self.stock_data.carryforward_nol
        net_income[0] = min(ebit_income[0], ebit_income[0] * (1 - tax_rate[0]))

        # Vettori completi
        revenue_growth = np.append(
            self.dcf_assumptions.revenue_growth, self.dcf_terminal.revenue_growth
        )
        operating_margin = np.append(
            self.dcf_assumptions.operating_margin, self.dcf_terminal.operating_margin
        )
        tax_rate = np.append(self.dcf_assumptions.tax_rate, self.dcf_terminal.tax_rate)
        sales_to_capital_ratio = np.append(
            self.dcf_assumptions.sales_to_capital_ratio,
            self.dcf_terminal.sales_to_capital_ratio,
        )

        for i in range(1, years):
            revenues[i] = revenues[i - 1] * (1 + revenue_growth[i - 1])
            ebit_income[i] = revenues[i] * operating_margin[i - 1]
            net_income[i] = min(
                ebit_income[i],
                ebit_income[i] - (ebit_income[i] - nol[i - 1]) * tax_rate[i - 1],
            )
            nol[i] = max(0, nol[i - 1] - ebit_income[i])

        for i in range(1, years - 1):
            reinvestment[i] = max(
                0,
                (revenues[i + 1] - revenues[i]) / sales_to_capital_ratio[i - 1],
            )
            fcff[i] = net_income[i] - reinvestment[i]

        i = years - 2
        # terminal year reinvestment
        reinvestment[i + 1] = max(
            0,
            (self.dcf_terminal.revenue_growth / self.dcf_terminal.return_on_capital)
            * net_income[i + 1],
        )
        fcff[i + 1] = net_income[i + 1] - reinvestment[i + 1]

        # Creare il DataFrame
        data = {
            "Revenues": revenues,
            "EBIT (Operating income)": ebit_income,
            "EBIT(1-t)": net_income,
            "Reinvestment": reinvestment,
            "FCFF": fcff,
            "NOL": nol,
        }

        self._future_financials = pd.DataFrame(data)
