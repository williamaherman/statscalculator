import numpy

class Mean:


    def mean(data):
        # empty data list error
        if len(data)==0:
            raise ValueError("Data list can not be empty")
        return numpy.mean(data)