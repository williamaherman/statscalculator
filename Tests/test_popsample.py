import statistics
import unittest
import random
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from PopulationSample.SimpleRandom import SimpleRandom\


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5, 6]
        random.seed(1)


    def test_simpRandSamp(self):
        result = SimpleRandom.SimpRandSamp(3, 3, self.test)
        x = None
        for i in result:
            if i in self.test:
                x = True
            else:
                x = False
        self.assertEqual(True, x)
        print("Simple Random Sampling Tested Successfully!")

if __name__ == '__main__':
    unittest.main()