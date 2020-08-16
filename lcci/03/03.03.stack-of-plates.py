class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.array = []

    def push(self, val: int) -> None:
        # 处理边界情况：cap == 0 不让push
        if self.cap == 0:
            return

        if not self.array or len(self.array[-1]) >= self.cap:
            self.array.append([val])
        else:
            self.array[-1].append(val)

    def pop(self) -> int:
        val = -1
        if self.array and self.array[-1]:
            val = self.array[-1].pop()
            if not self.array[-1]: self.array.pop()
        return val

    def popAt(self, index: int) -> int:
        val = -1
        if len(self.array) >= index + 1:
            val = self.array[index].pop()
            if not self.array[index]: self.array.pop(index)
        return val




if __name__ == '__main__':
    # Your StackOfPlates object will be instantiated and called as such:
    obj = StackOfPlates(2)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.popAt(0))
    print(obj.popAt(0))
    print(obj.popAt(0))

    obj = StackOfPlates(1)
    obj.push(1)
    obj.push(2)
    print(obj.popAt(1))
    print(obj.pop())
    print(obj.pop())
