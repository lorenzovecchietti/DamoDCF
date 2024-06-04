import unittest

from damo_dcf import dcf_calculator


class DamoDCFTests(unittest.TestCase):

  def test_01(self):
    # Test DCF from TOML. No options outstanding, no R&D capitalization.
    wbd = dcf_calculator.DCFCalculator("_unittest/assets/wbd1.toml")
    assert wbd is not None
    wbd_financials, fair_capitalization, fair_stock = wbd.run_dcf()
    assert not wbd_financials.empty
    assert abs(fair_capitalization+1758307933610.1577)<0.001
    assert abs(fair_stock+7.206180055779335)<0.01


if __name__ == '__main__':
  unittest.main()
