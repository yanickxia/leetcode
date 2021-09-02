from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding

    def next(self, n: int) -> int:
        if len(self.encoding) == 0:
            return -1

        r = self.encoding[0] - n
        if r < 0:
            self.encoding = self.encoding[2:]
            return self.next(abs(r))
        if r == 0:
            ret = self.encoding[1]
            self.encoding = self.encoding[2:]
            return ret
        else:
            self.encoding[0] = r
            return self.encoding[1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

if __name__ == '__main__':
    obj = RLEIterator(encoding=[3, 8, 0, 9, 2, 5])
    obj.next(2)
    obj.next(1)
    obj.next(1)
    print(obj.next(2))
