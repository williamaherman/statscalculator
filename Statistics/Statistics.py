from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.Median import median


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result
