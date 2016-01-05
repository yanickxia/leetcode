# coding=utf-8
__author__ = 'yann'


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_max = max(nums)
        lst = [0] * (num_max + 1)

        for n in nums:
            lst[n] = 1

        for i in range(0, num_max + 1):
            if lst[i] == 0:
                return i
        return num_max + 1



s = Solution()

print(s.missingNumber([0, 1, 3]))
print(s.missingNumber([0]))
