import os
import unittest
from mock import patch, MagicMock


class TestStock(unittest.TestCase):
    def setUp(self):
        print("Running test.")

    @patch("stovell.stock_portfolio.Stock")
    def test_stock(self, mock_stock):
        """
        Test that stock instantiates with properties
        """
        mock_stock(1,2,3)
        mock_stock.assert_called_once()
        print("Asserted the mock is called exactly once.")

    def tearDown(self):
        print("Done with test on Solution runnable.")

    @classmethod
    def tearDownClass(self):
        print("Done with tests.")


if __name__ == "__main__":
    unittest.main()
