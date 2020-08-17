from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        rs = [0 for i in range(len(nums))]
        for n in nums:
            if rs[n] == 1:
                return n
            else:
                rs[n] += 1

