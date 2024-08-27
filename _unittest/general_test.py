import pytest

from damo_dcf import dcf_calculator, option_calculator
from damo_dcf.dcf_calculator import DCFAssumptions
from damo_dcf.option_calculator import OptionData


def test_01():
    # Test DCF from TOML. No options outstanding, no R&D capitalization.
    amzn_file = "_unittest/assets/amzn.toml"
    amzn = dcf_calculator.initialize_dcf_from_toml(amzn_file)
    assert amzn is not None
    ev = amzn.run()
    ff = amzn.compute_future_financials()
    assert ff is not None
    assert abs(ev - 979883353664.1257) < 0.001
    assert (dcf_calculator.run_dcf_from_toml(amzn_file) - ev) < 0.001


def test_02_options_class():
    aapl_sigma = option_calculator.compute_stock_sigma("AAPL")
    assert aapl_sigma
    option = option_calculator.OptionData(k=1.8, t=1.5, sigma=aapl_sigma, n_o=int(2e3))
    assert option is not None
    option.sigma = 0.12
    assert abs(option.black_scholes_call(6, 0.03, 0.04, int(3e5)) - 4.014) < 0.001


def test_03_dcf_with_options():
    wbd = dcf_calculator.initialize_dcf_from_toml("_unittest/assets/wbd1.toml")
    wbd.option_data = OptionData(k=8.67, t=2.5, sigma=0.1, n_o=int(4.10 * 10e10))
    assert (wbd.run() + 1758307933610.995) < 0.001

    wbd = dcf_calculator.initialize_dcf_from_toml("_unittest/assets/wbd2.toml")
    assert (wbd.run() + 1758307933610.995) < 0.001


def test_04_failed_initialization():
    with pytest.raises(ValueError):
        DCFAssumptions(
            revenue_growth=[1, 2],
            operating_margin=[1, 2, 3],
            sales_to_capital_ratio=[1, 2],
            tax_rate=[1, 2],
            cost_of_capital=[1, 2],
        )


def test_05_failure_calculation():
    wbd = dcf_calculator.initialize_dcf_from_toml("_unittest/assets/wbd3.toml")
    assert wbd.failure_data is not None
    assert (wbd.failure_data.compute_failure(100000, 50000, 50000) - 80000.0) < 0.001
    wbd.failure_data.proceeds_value = "fair"
    assert (wbd.failure_data.compute_failure(1000000, 50000, 50000) - 800000.0) < 0.001
