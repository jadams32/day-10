import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(60, 40), 100.0)
        self.assertEqual(calculator.add(-60, 40), -20.0)
        self.assertEqual(calculator.add(60.5, 40), 100.5)



if __name__ =='__main__':
    unittest.main()