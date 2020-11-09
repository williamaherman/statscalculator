import statistics
import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()
        self.modeData = CsvReader('Tests/Data/modeData.csv').data
        self.medianData = CsvReader('Tests/Data/medianData.csv').data
        self.varianceData = CsvReader('Tests/Data/varianceData.csv').data
        self.standardDeviationData = CsvReader('Tests/Data/standdev.csv').data

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 4.25)

    def test_median_statistics(self):
        for row in self.medianData:
            result = row["Median"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "Median":
                    data.append(row[k])
            self.assertEqual(self.statistics.median(data), float(result))
        print("Median Tested Successfully!")

    def test_mode_statistics(self):
        for row in self.modeData:
            result = row["Mode"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "Mode":
                    data.append(row[k])
            self.assertEqual(self.statistics.mode(data), float(result))
        print("Mode Tested Successfully!")

    def test_variance(self):
            for row in self.varianceData:
                result = row["Variance"]
                data = []
                keys = row.keys()
                for k in keys:
                    if k != "Variance":
                        data.append(row[k])
                self.assertEqual(self.statistics.variance(data), float(result))
            print("Variance Tested Successfully!")

    def test_standard_deviation_statistics(self):
        for row in self.standardDeviationData:
            result = row["StandardDeviation"]
            data = []
            keys = row.keys()
            for k in keys:
                if k != "StandardDev":
                    data.append(row[k])
            self.assertEqual(self.statistics.standardDeviation(data), float(result))
        print("Standard Deviation Tested Successfully!")

if __name__ == '__main__':
    unittest.main()