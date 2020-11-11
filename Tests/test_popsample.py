import statistics
import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from PopulationSample.MarginOfError import MarginOfError


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5, 6]

    def test_marginOfError(self):
        result = MarginOfError.MarginOfError(2, self.test)
        self.assertEqual(result, -2.5)

if __name__ == '__main__':
    unittest.main()