import unittest
from unittest.mock import patch
from ex3_smelly import Clothing, Electronics, Grocery

class TestElectronics(unittest.TestCase):
    def setUp(self):
        self.electronic_item = Electronics("Laptop", 1000)

    @patch('builtins.print')
    def test_apply_discount(self, mock_print):
        # Expected discount price for Electronics (10% off of 1000)
        expected_price = 1000 - (1000 * 0.10)
        self.assertAlmostEqual(self.electronic_item.apply_discount(), expected_price, places=2)
        mock_print.assert_any_call("Discounted price for Laptop (Electronics): 900.0")

    @patch('builtins.print')
    def test_calculate_tax(self, mock_print):
        # Expected tax for Electronics (15% on 1000)
        expected_tax = 1000 * 0.15
        self.assertAlmostEqual(self.electronic_item.calculate_tax(), expected_tax, places=2)
        mock_print.assert_any_call("Tax for Laptop (Electronics): 150.0")


class TestClothing(unittest.TestCase):
    def setUp(self):
        self.clothing_item = Clothing("Shirt", 50)

    @patch('builtins.print')
    def test_apply_discount(self, mock_print):
        # Expected discount price for Clothing (20% off of 50)
        expected_price = 50 - (50 * 0.20)
        self.assertAlmostEqual(self.clothing_item.apply_discount(), expected_price, places=2)
        mock_print.assert_any_call("Discounted price for Shirt (Clothing): 40.0")

    @patch('builtins.print')
    def test_calculate_tax(self, mock_print):
        # Expected tax for Clothing (8% on 50)
        expected_tax = 50 * 0.08
        self.assertAlmostEqual(self.clothing_item.calculate_tax(), expected_tax, places=2)
        mock_print.assert_any_call("Tax for Shirt (Clothing): 4.0")


class TestGrocery(unittest.TestCase):
    def setUp(self):
        self.grocery_item = Grocery("Milk", 10)

    @patch('builtins.print')
    def test_apply_discount(self, mock_print):
        # Expected discount price for Grocery (5% off of 10)
        expected_price = 10 - (10 * 0.05)
        self.assertAlmostEqual(self.grocery_item.apply_discount(), expected_price, places=2)
        mock_print.assert_any_call("Discounted price for Milk (Grocery): 9.5")

    @patch('builtins.print')
    def test_calculate_tax(self, mock_print):
        # Expected tax for Grocery (2% on 10)
        expected_tax = 10 * 0.02
        self.assertAlmostEqual(self.grocery_item.calculate_tax(), expected_tax, places=2)
        mock_print.assert_any_call("Tax for Milk (Grocery): 0.2")
        


if __name__ == '__main__':
    unittest.main()
