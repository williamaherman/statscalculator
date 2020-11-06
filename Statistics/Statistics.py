from Calculator.Calculator import Calculator
from Statistics.Mean import mean


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__():

    def mean(self, data):
        self.result = mean(data)
        return self.result