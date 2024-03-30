import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.num.get(val) is not None:
            return False
        self.num[val] = val
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.num.get(val) is None:
            return False
        del self.num[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        keys = self.num.keys()
        if len(keys) == 0:
            return 0

        i = random.randint(0, len(keys) - 1)
        return self.num[list(keys)[i]]


# Your RandomizedSet object will be instantiated and called as such:
if __name__ == '__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(1)
    param_3 = obj.getRandom()
