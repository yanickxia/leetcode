class SortedStack:

    def __init__(self):
        self.stack = []
        self.tmp = []

    def push(self, val: int) -> None:
        if self.isEmpty():
            self.stack.append(val)
        else:
            while self.stack:
                x = self.stack.pop()
                if x < val:
                    self.tmp.append(x)
                else:
                    self.stack.append(x)
                    break
            self.stack.append(val)

            while self.tmp:
                self.stack.append(self.tmp.pop())

    def pop(self) -> None:
        if self.isEmpty():
            return None
        self.stack.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

if __name__ == '__main__':
    obj = SortedStack()
    obj.push(1)
    obj.push(2)
    obj.push(2)
    obj.push(3)
    obj.push(3)

    print(obj.peek())
    print(obj.pop())
    print(obj.peek())