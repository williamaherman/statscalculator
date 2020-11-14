from Calculator.SquareRoot import square_root
from Statistics.Mean import mean
from Statistics.StandardDeviation import standardDeviation


def top_interval(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = standardDeviation(num)
        avg = mean(num)
        return round(avg + (z * sd / square_root(num_values)), 5)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0")
    except ValueError:
        print("Error: Check data input")