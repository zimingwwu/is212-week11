import unittest
from unittest.mock import patch
from ex1_refactored import OrderProcessor


class TestOrderProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = OrderProcessor()

    def test_process_order_without_customer_id(self):
        order = {
            "items": [{"id": 1, "name": "Widget", "price": 20.0, "quantity": 2}]
        }
        with self.assertRaises(ValueError):
            self.processor.process_order(order)

    def test_process_order_without_items(self):
        order = {
            "customer_id": 12345,
            "items": []
        }
        with self.assertRaises(ValueError):
            self.processor.process_order(order)

    @patch('builtins.print')
    def test_process_order_with_valid_order(self, mock_print):
        order = {
            "customer_id": 12345,
            "items": [
                {"id": 1, "name": "Widget", "price": 20.0, "quantity": 2},
                {"id": 2, "name": "Gadget", "price": 15.0, "quantity": 1}
            ]
        }
        receipt = self.processor.process_order(order)

        expected_receipt = (
            "Customer ID: 12345\n"
            "Items:\n"
            "- Widget: 2 x $20.0\n"
            "- Gadget: 1 x $15.0\n"
            "Total: $55.00\n"
        )

        self.assertEqual(receipt, expected_receipt)
        mock_print.assert_any_call("Updating inventory for item 1, reducing stock by 2.")
        mock_print.assert_any_call("Updating inventory for item 2, reducing stock by 1.")
        mock_print.assert_called_with("Sending email to customer 12345 with receipt:\nCustomer ID: 12345\nItems:\n- Widget: 2 x $20.0\n- Gadget: 1 x $15.0\nTotal: $55.00\n")

    @patch('builtins.print')
    def test_process_order_with_discount_code(self, mock_print):
        order = {
            "customer_id": 12345,
            "items": [
                {"id": 1, "name": "Widget", "price": 50.0, "quantity": 1}
            ],
            "discount_code": "SUMMER20"
        }
        receipt = self.processor.process_order(order)

        expected_receipt = (
            "Customer ID: 12345\n"
            "Items:\n"
            "- Widget: 1 x $50.0\n"
            "Total: $40.00\n"
        )

        self.assertEqual(receipt, expected_receipt)
        mock_print.assert_any_call("Updating inventory for item 1, reducing stock by 1.")
        mock_print.assert_called_with("Sending email to customer 12345 with receipt:\nCustomer ID: 12345\nItems:\n- Widget: 1 x $50.0\nTotal: $40.00\n")

if __name__ == '__main__':
    unittest.main()
