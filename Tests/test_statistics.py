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
        self.statistics = Statistics()
        self.modeData= CsvReader('Tests/Data/modeData.csv').data
        self.medianData = CsvReader('Tests/Data/medianData.csv').data


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)

    def test_mode_statistics(self):
        for row in self.modeData:
            result = row["Mode"]
            data = []
            keys = row.keys()
            for x in keys:
                if x != "Mode":
                    data.append(row[x])
            self.assertEqual(self.statistics.mode(data), float(result))
        print("Mode Tested Successfully!")

    def test_median_statistics(self):
        for row in self.medianData:
            result = row["Median"]
            data = []
            keys = row.keys()
            for x in keys:
                if x != "Median":
                    data.append(row[x])
                self.assertEqual(self.statistics.median(data), float(result))
            print("Median Tested Successfully!")


if __name__ == '__main__':
    unittest.main()