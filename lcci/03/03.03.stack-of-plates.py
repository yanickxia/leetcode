class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stacks = []
        self.curr = 0

    def push(self, val: int) -> None:
        if self.cap == 0:
            return

        mod = int(self.curr / self.cap)
        if len(self.stacks) <= mod:
            self.stacks.append([])

        self.stacks[mod].append(val)

        self.curr += 1

    def pop(self) -> int:
        if self.cap == 0:
            return -1

        if len(self.stacks) == 0:
            return -1
        stack = self.stacks[-1]
        x = stack.pop()
        if len(stack) == 0:
            self.stacks = self.stacks[0:len(self.stacks)-1]
        self.curr -=1
        return x


    def popAt(self, index: int) -> int:
        if self.cap == 0:
            return -1
        if index > len(self.stacks) -1:
            return -1

        stack = self.stacks[index]
        x = stack.pop()

        reput = []
        for i in range(index+1, len(self.stacks)):
            while self.stacks[i]:
                reput.append(self.stacks[i].pop())
                self.curr -=1

        for i in range(index + 1, len(self.stacks)):
            del self.stacks[i]

        for re in reput:
            self.push(re)

        if len(self.stacks[-1]) == 0:
            self.stacks = self.stacks[0:len(self.stacks)-1]

        self.curr -=1
        return x



if __name__ == '__main__':
    # Your StackOfPlates object will be instantiated and called as such:
    obj = StackOfPlates(2)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.popAt(0))
    print(obj.popAt(0))
    print(obj.popAt(0))