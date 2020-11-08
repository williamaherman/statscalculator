from Calculator.Addition import addition

def mode(num):
    counter = {}
    for n in num:
        if n in counter:
            counter[n] = addition(counter[n],1)
        else:
            counter[n] = 1
    result = None
    maxCount = 0
    for k in counter.keys():
        if counter[k] > maxCount:
            maxCount = counter[k]
            result = k
    return float(result)