import statistics
import unittest
import random
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from PopulationSample.MarginOfError import marginofError
from PopulationSample.SimpleRandom import SimpleRandom



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5, 6]
        random.seed(1)

    def test_margin(self):
        test_data = CsvReader('./Tests/Data/MoEData.csv').data
        for row in test_data:
            self.assertEqual(
                self.(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5']),
                float(row['MoE']))
            self.assertEqual(self.PopulationSample.result, float(row['MoE']))
        test_data.clear()

    def test_simpRandSamp(self):
        result = SimpleRandom.SimpRandSamp(3, 3, self.test)
        x = None
        for i in result:
            if i in self.test:
                x = True
            else:
                x = False
        self.assertEqual(True, x)

if __name__ == '__main__':
    unittest.main()