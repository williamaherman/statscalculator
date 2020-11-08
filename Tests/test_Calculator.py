import unittest
import sys

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_Mean(self):
        self.assertEqual(round(statistics.mean(self.rand_test), 6), round(Mean.mean(self.rand_test), 6))
        self.rand_test = self.rand_test + RandList.randListFloat(length=3, seed=1, lower=1, upper=100)
        self.assertEqual(round(statistics.mean(self.rand_test), 6), round(Mean.mean(self.rand_test), 6))

if __name__ == '__main__':
    unittest.main()