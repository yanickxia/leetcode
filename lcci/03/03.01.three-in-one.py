class TripleInOne:

    def __init__(self, stackSize: int):
        self.TripleStack = [[] for i in range(3)]
        self.stackSize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.TripleStack[stackNum]) < self.stackSize:
            self.TripleStack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.TripleStack[stackNum] != []:
            cache = self.TripleStack[stackNum][-1]
            self.TripleStack[stackNum] = self.TripleStack[stackNum][:-1]
            return cache
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        if self.TripleStack[stackNum] != []:
            cache = self.TripleStack[stackNum][-1]
            return cache
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.TripleStack[stackNum] == []


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)