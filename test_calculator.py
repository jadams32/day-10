import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(60, 40), 100.0)
        self.assertEqual(calculator.add(-60, 40), -20.0)
        self.assertEqual(calculator.add(60.5, 40), 100.5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(60, 40), 20.0)
        self.assertEqual(calculator.subtract(-60, 40), -100.0)
        self.assertEqual(calculator.subtract(60.5, 40), 20.5)

    def test_multiply(self):
        self.assertEqual(calculator.multi(60, 40), 2400)
        self.assertEqual(calculator.multi(-60, 40), -2400)
        self.assertEqual(calculator.multi(60.5, 40), 2420)

    def test_division(self):
        self.assertEqual(calculator.division(60, 40), 1.5)
        self.assertEqual(calculator.division(-60, 40), -1.5)
        self.assertEqual(calculator.division(60.5, 40), 1.5125)


if __name__ == '__main__':
    unittest.main()
