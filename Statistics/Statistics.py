from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.Median import median
from Statistics.Variance import variance
from Statistics.Zscore import zscore
from Statistics.StandardDeviation import standardDeviation
from PopulationSample.ConfidenceIntervalTop import top_interval
from PopulationSample.ConfidenceIntervalBottom import bottom_interval

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

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def zscore(self, data):
        self.result = zscore(data)

    def standardDeviation(self, data):
        self.result = standardDeviation(data)
        return self.result

    def confidence_interval_top(self, data):
        self.result = top_interval(data)
        return self.result

    def confidence_interval_bottom(self, data):
        self.result = bottom_interval(data)
        return self.result

        return self.result
