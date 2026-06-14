import unittest
import app
import math

class TestCAGR(unittest.TestCase):
    def test_calculate_cagr_valid(self):
        result = app.calculate_cagr('AAPL')
        self.assertIn('cagr', result)
        self.assertIsInstance(result['cagr'], float)
        self.assertNotEqual(result['starting_value'], 0)
        self.assertNotEqual(result['final_value'], 0)
        self.assertIn('start_date', result)
        self.assertIn('end_date', result)

    def test_calculate_cagr_search(self):
        result = app.calculate_cagr('Apple')
        self.assertIn('cagr', result)
        self.assertEqual(result.get('ticker'), 'AAPL')

    def test_calculate_cagr_invalid(self):
        result = app.calculate_cagr('INVALID_TICKER_XYZ_123')
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
