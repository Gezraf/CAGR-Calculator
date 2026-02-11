import unittest
import app
import math

class TestCAGR(unittest.TestCase):
    def test_calculate_cagr_valid(self):
        # We can't easily mock yfinance without external libraries or complex mocking, 
        # so for this integration test we'll use a stable ticker like 'AAPL' 
        # and check if it returns the expected structure and non-zero values.
        result = app.calculate_cagr('AAPL')
        self.assertIn('cagr', result)
        self.assertIsInstance(result['cagr'], float)
        self.assertNotEqual(result['starting_value'], 0)
        self.assertNotEqual(result['final_value'], 0)
        self.assertIn('start_date', result)
        self.assertIn('end_date', result)

    def test_calculate_cagr_search(self):
        # Search for "Apple" should return AAPL or similar
        result = app.calculate_cagr('Apple')
        self.assertIn('cagr', result)
        self.assertEqual(result.get('ticker'), 'AAPL')

    def test_calculate_cagr_invalid(self):
        # Test with a nonsense string that shouldn't match anything
        result = app.calculate_cagr('INVALID_TICKER_XYZ_123')
        # Depending on yfinance search, it might return empty or error
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
