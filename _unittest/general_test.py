import unittest

import numpy as np

from damo_dcf import dcf_calculator, option_calculator


class DamoDCFTests(unittest.TestCase):

    def test_01(self):
        # Test DCF from TOML. No options outstanding, no R&D capitalization.
        wbd = dcf_calculator.run_dcf_from_toml("_unittest/assets/wbd1.toml")
        assert wbd is not None
        ev=wbd.run_dcf()
        ff=wbd.future_financials()
        assert ff is not None
        assert abs(ev + 1758307933610.157) < 0.001
        assert abs(ev/wbd.stock_data.number_of_shares_outstanding + 7.206) < 0.001

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
