import unittest

import numpy as np

from damo_dcf import dcf_calculator, option_calculator


class DamoDCFTests(unittest.TestCase):

    def test_01(self):
        # Test DCF from TOML. No options outstanding, no R&D capitalization.
        wbd = dcf_calculator.DCFCalculator("_unittest/assets/wbd1.toml")
        assert wbd is not None
        wbd.run_dcf()        
        assert wbd.future_financials is not None
        assert abs(wbd.equity_value + 1758307933610.157) < 0.001
        assert abs(wbd.stock_value + 7.206) < 0.001

    def test_02_options(self):
        aapl_sigma = option_calculator.compute_stock_sigma("AAPL")
        assert aapl_sigma
        option = option_calculator.OptionData(
            k=1.8, t=1.5, ticker_symbol="AAAAAPL", n_o=int(2e3)
        )
        assert np.isnan(option.sigma)
        option = option_calculator.OptionData(
            k=1.8, t=1.5, ticker_symbol="AAPL", n_o=int(2e3)
        )
        assert option is not None
        assert option.sigma == aapl_sigma
        option.sigma = 0.12
        assert abs(option.black_scholes_call(6, 0.03, 0.04, int(3e5)) - 4.014) < 0.001


if __name__ == "__main__":
    unittest.main()
