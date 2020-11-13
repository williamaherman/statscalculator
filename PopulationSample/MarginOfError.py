from Statistics import Zscore, StandardDeviation
from Statistics.StandardDeviation import standardDeviation


def marginofError(self, a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        data = [a, b, c, d, e]

        n = len([data])
        num2 = self.standardDeviation([a, b, c, d, e])
        num3 = round(self.square_root(n), 6)
        value1 = self.division(num3, num2)
        z = int(1.96)
        self.result = round(self.multiplication(value1, z), 6)

    except ZeroDivisionError:
        print("Error. Cannot Divide by 0")
    except ValueError:
        print("Error. Invalid data inputs")
    return self.result