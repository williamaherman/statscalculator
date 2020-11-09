from Statistics.Mean import mean
from Calculator.Square import square
from Calculator.Subtraction import subtraction

def variance(num):
    Mean_var = mean(num)

    Man = []
    for n in num:
        Variables = subtraction(n, Mean_var)
        Man.append(Variables)

    Squares = []
    for Variables in Man:
        Square_var = square(Variables)
        Squares.append(Square_var)

    return mean(Squares)