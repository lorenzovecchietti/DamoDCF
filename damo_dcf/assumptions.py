import numpy as np
from pydantic import BaseModel, ConfigDict, field_validator, model_validator


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
    revenue_growth: np.ndarray
    operating_margin: np.ndarray
    sales_to_capital_ratio: np.ndarray
    tax_rate: np.ndarray
    cost_of_capital: np.ndarray

    @field_validator(
        "revenue_growth",
        "operating_margin",
        "sales_to_capital_ratio",
        "tax_rate",
        "cost_of_capital",
        mode="before",
    )
    def make_ndarray(cls, v):
        v = np.asarray(v)
        if len(v.shape) == 1:
            v = v.reshape(1, v.shape[0])
        return v

    @model_validator(mode="after")
    def check_equal_length(self) -> "DCFAssumptions":
        arrays = [
            self.__getattribute__(field)
            for field in [
                "revenue_growth",
                "operating_margin",
                "tax_rate",
                "cost_of_capital",
                "sales_to_capital_ratio",
            ]
        ]
        if (
            len({arr_len := array.shape[-1] for array in arrays[:-1]}) > 1
            or arrays[-1].shape[-1] > arr_len
            or arrays[-1].shape[-1] < arr_len - 1
        ):
            raise ValueError(
                "All arrays must have the same length except for "
                "sales_to_capital_ratio for which terminal year value is not needed."
            )
        elif arr_len == arrays[-1].shape[-1]:
            print(
                "Terminal year value for sales_to_capital_ratio is not needed "
                "and will be ignored"
            )
            self.sales_to_capital_ratio = self.sales_to_capital_ratio[:, :-1]
        return self
