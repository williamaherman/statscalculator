from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def median(num):
    num.sort()
    length = len(num)
    result = None
    index1 = int(division(2, length))
    if length % 2 == 0:
        index2 = int(subtraction(index1, 1))
        value1 = num[index1]
        value2 = num[index2]
        result = mean([value1, value2])
    else:
        result = num[index1]
    return float(result)