from datetime import datetime, timedelta
from typing import Optional

import numpy as np
import yfinance as yf
from pydantic import BaseModel
from scipy.stats import norm


def compute_stock_sigma(stock_name: str) -> float:
    # Fetch historical price data for the stock to compute std dev
    today = datetime.now()
    one_year_ago = today - timedelta(days=365)
    close = yf.download(
        stock_name,
        end=today.strftime("%Y-%m-%d"),
        start=one_year_ago.strftime("%Y-%m-%d"),
    )["Adj Close"]
    std_dev = float(np.std(close))
    return std_dev


class OptionData(BaseModel):
    k: float  # average strike price
    t: float  # average time to maturity in years
    sigma: Optional[float]
    n_o: int  # number of warrants outstanding

    def __init__(self, k: float, t: float, ticker_symbol: str, n_o: int):
        try:
            sigma = compute_stock_sigma(ticker_symbol)
        except Exception:
            print("No std deviation computed. Set it manually.")
            sigma = None
        super().__init__(k=k, t=t, sigma=sigma, n_o=n_o)

    def black_scholes_call(
        self,
        s: float,  # current stock price
        q: float,  # annualized dividend
        r: float,  # risk free rate
        n_s: int,  # number of shares outstanding
    ) -> float:
        if self.sigma is None:
            raise AttributeError("Assign a value to the sigma field.")
        s = (s * n_s + self.k * self.n_o) / (n_s + self.n_o)
        d1 = (np.log(s / self.k) + (r - q + 0.5 * self.sigma**2) * self.t) / (
            self.sigma * np.sqrt(self.t)
        )
        print(d1)
        d2 = d1 - self.sigma * np.sqrt(self.t)
        print(d2)

        call_price = (s * np.exp(-q * self.t) * norm.cdf(d1)) - (
            self.k * np.exp(-r * self.t) * norm.cdf(d2)
        )
        return call_price
