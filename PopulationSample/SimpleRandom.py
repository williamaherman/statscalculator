import random
from RanNumGen.RanNumGenHelper import ListPick

class SimpleRandom:

    @staticmethod
    def SimpRandSamp(seed, nums, data):
        if len(data)==0:
            raise ValueError("Data list can not be empty.")
        random.seed(seed)
        return ListPick.listPickListSeed(seed, nums, data)

    @staticmethod
    def listPickSeed(seed, data):
        random.seed(seed)
        return ListPick.listPick(data)

    @staticmethod
    def listPickListSeed(seed, nums, data):
        random.seed(seed)
        return ListPick.listPickList(nums, data)