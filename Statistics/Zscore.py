from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.StandardDeviation import standardDeviation
from Statistics.Mean import mean

def zscore(num):
    meanEst = mean(num)
    standardDeviation_var = standardDeviation(num)

    negative = []
    for var in num:
        meaneasy = subtraction(meanEst, var)
        negative.append(meaneasy)

    ZScore_fun = []
    for neg in negative:
        z = division(standardDeviation_var, neg)
        ZScore_fun.append(z)

    return ZScore_fun