import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------

    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_standard_default(self):
        # Calling without service= must still return standard pricing.
        self.assertEqual(shipping_quote(1, "regional"), 9.5)

    # ------------------------------------------------------------------
    # Express service ($7 surcharge on top of standard)
    # ------------------------------------------------------------------

    def test_express_local(self):
        # local base 5 + 7 surcharge + 1.5*2 = 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # regional base 8 + 7 surcharge + 1.5*2 = 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # local base 5 + 7 + 1.5*0.5 = 12.75
        self.assertEqual(shipping_quote(0.5, "local", service="express"), 12.75)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def test_invalid_weight_zero(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_weight_negative(self):
        with self.assertRaises(ValueError):
            shipping_quote(-1, "regional")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
