from Calculator.SquareRoot import square_root
from Statistics.Variance import variance

def standardDeviation(data):
    var = variance(data)
    return round(square_root(var), 2)