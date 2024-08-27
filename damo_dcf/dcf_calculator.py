from typing import Optional

import numpy as np
import pandas as pd
import toml
from pydantic import BaseModel, ConfigDict

from damo_dcf.assumptions import DCFAssumptions, MarketData, StockData
from damo_dcf.failure_calculator import FailureData
from damo_dcf.option_calculator import OptionData


class DCFCalculator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    ticker_symbol: str
    multiplier: int
    stock_data: StockData
    current_stock_price: float
    dcf_assumptions: DCFAssumptions
    market_data: MarketData
    option_data: Optional[OptionData] = None
    failure_data: Optional[FailureData] = None

    @property
    def _years_to_predict(self) -> int:
        return self.dcf_assumptions.revenue_growth.size

    def run(self) -> float:
        future_financials = self.compute_future_financials()
        pv_sum = sum(future_financials["PV FCFF"].values)
        failure_probability = (
            self.failure_data.failure_probability
            if self.failure_data is not None
            else 0
        )
        failure_proceeds = (
            self.failure_data.compute_failure(
                pv=pv_sum,
                book_value=self.stock_data.book_value_of_equity,
                book_debt=self.stock_data.book_value_of_debt,
            )
            if self.failure_data is not None
            else 0
        )
        equity_value = (
            pv_sum * (1 - failure_probability)
            + failure_probability * failure_proceeds
            - self.stock_data.book_value_of_debt
            + -self.stock_data.minority_interests
            + self.stock_data.cash_and_marketable_securities
            + self.stock_data.cross_holdings_and_other_non_operating_assets
        )
        if self.option_data is not None:
            equity_value -= self.option_data.black_scholes_call(
                self.current_stock_price,
                self.stock_data.annualized_dividend,
                self.market_data.riskfree_rate,
                self.stock_data.number_of_shares_outstanding,
            )
        return equity_value

    def compute_future_financials(self) -> pd.DataFrame:
        years = self._years_to_predict

        # Pointers
        tax_rate = self.dcf_assumptions.tax_rate
        sales_to_capital_ratio = self.dcf_assumptions.sales_to_capital_ratio
        operating_margin = self.dcf_assumptions.operating_margin
        revenue_growth = self.dcf_assumptions.revenue_growth

        # Initialize
        reinvestment = np.zeros(years)
        pv_fcf = np.zeros(years)

        revenues = self.stock_data.revenue * np.cumprod(1 + revenue_growth, axis=0)
        ebit_income = revenues * operating_margin
        nol = np.maximum(0, self.stock_data.carryforward_nol - np.cumsum(ebit_income))
        net_income = np.minimum(
            ebit_income,
            ebit_income - (ebit_income - nol) * tax_rate,
        )

        reinvestment[:-1] = np.ediff1d(revenues) / sales_to_capital_ratio
        reinvestment[-1] = (
            self.dcf_assumptions.revenue_growth[-1]
            / self.dcf_assumptions.cost_of_capital[-1]
            * net_income[-1]
        )
        reinvestment = np.maximum(0, reinvestment)

        fcff = net_income - reinvestment
        cum_disc_factor = np.cumprod(
            1 / (1 + self.dcf_assumptions.cost_of_capital[:-1])
        )
        pv_fcf[:-1] = fcff[:-1] * cum_disc_factor
        pv_fcf[-1] = (
            fcff[-1]
            / (
                self.dcf_assumptions.cost_of_capital[-1]
                - self.dcf_assumptions.revenue_growth[-1]
            )
            * cum_disc_factor[-1]
        )

        # Creare il DataFrame
        data = {
            "Revenues": revenues,
            "EBIT (Operating income)": ebit_income,
            "EBIT(1-t)": net_income,
            "Reinvestment": reinvestment,
            "FCFF": fcff,
            "NOL": nol,
            "PV FCFF": pv_fcf,
        }

        return pd.DataFrame(data)


def initialize_dcf_from_toml(input_toml: str) -> DCFCalculator:
    with open(input_toml, "r") as file:
        data = toml.load(file)
    financials = {k: v * data["multiplier"] for k, v in data["firm_data"].items()}
    if data.get("options", False):
        data["options"]["n_o"] = int(data["multiplier"] * data["options"]["n_o"])
        option_data = OptionData(**data["options"])
    else:
        option_data = None
    if data.get("failure", False):
        failure_data = FailureData(**data["failure"])
    else:
        failure_data = None
    return DCFCalculator(
        ticker_symbol=data["ticker_symbol"],
        multiplier=data["multiplier"],
        current_stock_price=data["current_stock_price"],
        stock_data=StockData(**financials),
        dcf_assumptions=DCFAssumptions(**data["future_assumptions"]),
        market_data=MarketData(**data["market_data"]),
        option_data=option_data,
        failure_data=failure_data,
    )


def run_dcf_from_toml(input_toml: str):
    dcf = initialize_dcf_from_toml(input_toml)
    return dcf.run()
