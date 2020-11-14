from Calculator.SquareRoot import square_root
from Statistics.Mean import mean
from Statistics.StandardDeviation import standardDeviation


def confidence_interval_top(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = standardDeviation(num)
        avg = mean(num)
        return round(avg + (z * sd / square_root(num_values)), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")