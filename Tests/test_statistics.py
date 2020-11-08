import statistics
import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.mode_value = statistics.mode(self.testData)
        self.statistics = Statistics()
        self.test_data_mode = CsvReader('Tests/Data/modeData.csv').data


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, self.mode_value)


if __name__ == '__main__':
    unittest.main()