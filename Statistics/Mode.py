from Calculator.Addition import addition

def mode(num):
    counter = {}
    for n in num:
        if n in counter:
            counter[n] = addition(counter[n],1)
        else:
            counter[n] = 1
    result = None
    timeout = 0
    for x in counter.keys():
        if counter[x] > timeout:
            timeout = counter[x]
            result = x
    return float(result)