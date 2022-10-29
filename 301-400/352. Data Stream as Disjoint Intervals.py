from typing import List


# time cost 45:47
class SummaryRanges:

    number = []

    def __init__(self):
        self.number = []

    def addNum(self, value: int) -> None:
        if len(self.number) == 0:
            self.number.append(value)
            return
        if value >= self.number[-1]:
            if value == self.number[-1]:
                return
            self.number.append(value)
            return
        if value < self.number[0]:
            if value == self.number[0]:
                return
            self.number.insert(0, value)
            return

        SummaryRanges.add_num(value, self.number)

    @staticmethod
    def add_num(val, numbers):
        begin = 0
        end = len(numbers) - 1

        while True:
            if begin+1 == end:
                if numbers[begin] == val:
                    return
                numbers.insert(begin + 1, val)
                return
            mid = int((end +begin) / 2)
            if numbers[mid] > val:
                end = mid
            else:
                begin = mid

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        i,j = 0,0
        while i < len(self.number):
            begin = self.number[i]
            while i+j < len(self.number) - 1 and (self.number[i+j] +1 ==  self.number[i+j+1] ):
                j += 1
            end = self.number[i+j]
            i += j + 1
            intervals.append([begin,end])
            j = 0
        return intervals



# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(6)
obj.addNum(6)
obj.addNum(0)
param_2 = obj.getIntervals()
print(param_2)