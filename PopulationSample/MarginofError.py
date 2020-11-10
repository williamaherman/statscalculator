from Statistics.StandardDeviation import standardDeviation
from Statistics.ZScore import ZScore


class MarginOfError:
    @staticmethod
    def marginOfError(seed, data):
        if len(data)==0:
            raise ValueError("Data list can not be empty")
        zsc = ZScore.zscore(seed, data)
        stddev = Stddev.stddev(data)
        return ZScore * standardDeviation