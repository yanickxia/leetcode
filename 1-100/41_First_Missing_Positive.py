# -*- coding:utf-8 -*-

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        ars = [0] * (max(nums) + 1)
        for n in nums:
            if n >= 0:
                ars[n] = 1

        for i in range(1, len(ars)):
            if ars[i] == 0:
                return i
        return len(ars)


s = Solution()
print(s.firstMissingPositive([1, 2, 0]))
print(s.firstMissingPositive([3,4,-1,1]))