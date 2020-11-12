from Statistics import Zscore, StandardDeviation
from Statistics.StandardDeviation import standardDeviation

class MarginOfError:
    @staticmethod
    def MarginOfError(seed, data):
        if len(data)==0:
            raise ValueError("Data list can not be empty")
        zsc = Zscore.zscore(seed, data)
        stddev = StandardDeviation.standardDeviation(data)
        return Zscore * standardDeviation