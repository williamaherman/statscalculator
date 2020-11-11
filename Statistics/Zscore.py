from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.StandardDeviation import standardDeviation
from Statistics.Mean import mean

def zscore(num):
    Mean_var = mean(num)
    standardDeviation_var = standardDeviation(num)

    negative = []
    for Raw_var in num:
        meanRaw = subtraction(Mean_var, Raw_var)
        negative.append(meanRaw)

    ZScore_var = []
    for neg in negative:
        z = division(standardDeviation_var, neg)
        ZScore_var.append(z)


    return ZScore_var