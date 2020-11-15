import random

class ListPick:

    @staticmethod
    def listPick(data):
        return random.choice(data)

    @staticmethod
    def listPickSeed(seed, data):
        random.seed(seed)
        return ListPick.listPick(data)

    @staticmethod
    def listPickList(nums, data):
        temp = []
        while len(temp) < nums:
            temp.append(ListPick.listPick(data))
        return temp

    @staticmethod
    def listPickListSeed(seed, nums, data):
        random.seed(seed)
        return ListPick.listPickList(nums, data)