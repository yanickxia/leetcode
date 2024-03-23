# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.callNum = 0

    def get(self, index: int) -> int:
        self.callNum += 1
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def __init__(self):
        self.cached = {}

    def getIndex(self, mountain_arr: 'MountainArray', index):
        if index in self.cached:
            return self.cached[index]
        val = mountain_arr.get(index)
        self.cached[index] = val
        return val

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lastIndex = mountain_arr.length() - 1
        left, right = self.getIndex(mountain_arr, 0), self.getIndex(mountain_arr, lastIndex)

        if left > target and right > target:
            return -1

        mountainTop = self.findMountainTop(mountain_arr, 0, mountain_arr.length() - 1)

        left = self.findInMountain(target, mountain_arr, 0, mountainTop, True)
        right = self.findInMountain(target, mountain_arr, mountainTop, (mountain_arr.length() - 1), False)
        if left != -1:
            return left
        if right != -1:
            return right
        return -1

    def findMountainTop(self, mountain_arr: 'MountainArray', leftIndex, rightIndex) -> int:
        if abs(leftIndex - rightIndex) == 1:
            if self.getIndex(mountain_arr, leftIndex) > self.getIndex(mountain_arr, rightIndex):
                return leftIndex
            return rightIndex

        midIndex = int((leftIndex + rightIndex) / 2)
        leftValue, midValue, rightValue = self.getIndex(mountain_arr, leftIndex), self.getIndex(mountain_arr, midIndex), self.getIndex(mountain_arr, rightIndex)
        if midValue < leftValue:
            return self.findMountainTop(mountain_arr, leftIndex, midIndex)
        return self.findMountainTop(mountain_arr, midIndex, rightIndex)

    def findInMountain(self, target: int, mountain_arr: 'MountainArray', leftIndex, rightIndex, isLeft):
        if abs(leftIndex - rightIndex) == 1:
            if self.getIndex(mountain_arr, leftIndex) == target:
                return leftIndex
            if self.getIndex(mountain_arr, rightIndex) == target:
                return rightIndex
            return -1
        leftValue = self.getIndex(mountain_arr, leftIndex)
        rightValue = self.getIndex(mountain_arr, rightIndex)
        midIndex = int((leftIndex + rightIndex) / 2)
        midValue = self.getIndex(mountain_arr, midIndex)
        found = midValue == target
        result = []
        if found:
            result.append(midIndex)

        if isLeft:
            # find left
            if leftValue <= target <= midValue:
                result.append(self.findInMountain(target, mountain_arr, leftIndex, midIndex, isLeft))
            if midValue <= target << rightValue:
                result.append(self.findInMountain(target, mountain_arr, midIndex, rightIndex, isLeft))
        else:
            if leftValue >= target >= midValue:
                result.append(self.findInMountain(target, mountain_arr, leftIndex, midIndex, isLeft))
            if midValue >= target >= rightValue:
                result.append(self.findInMountain(target, mountain_arr, midIndex, rightIndex, isLeft))

        result = [x for x in result if x != -1]
        if len(result) == 0:
            return -1

        return min(result)


if __name__ == '__main__':
    m = MountainArray([0, 5, 3, 1])
    s = Solution()
    print(s.findInMountainArray(1, m), 3)

    m = MountainArray([0, 5, 3, 1])
    s = Solution()
    print(s.findInMountainArray(0, m), 0)

    m = MountainArray([1, 2, 3, 4, 5, 3, 1])
    s = Solution()
    print(s.findInMountainArray(3, m), 2)

    m = MountainArray([1, 5, 2])
    s = Solution()
    print(s.findInMountainArray(2, m), 2)

    m = MountainArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2])
    s = Solution()
    print(s.findInMountainArray(1, m), 0, "callNumb", m.callNum)

    m = MountainArray([1, 5, 2])
    s = Solution()
    print(s.findInMountainArray(1, m), 0)

    m = MountainArray([1, 2, 3, 4, 5, 3, 1])
    s = Solution()
    print(s.findInMountainArray(3, m), 2)

    m = MountainArray([0, 1, 2, 4, 2, 1])
    s = Solution()
    print(s.findInMountainArray(3, m), -1)
