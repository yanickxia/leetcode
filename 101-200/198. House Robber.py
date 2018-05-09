# -*- coding:utf-8 -*-
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxS = [0] * len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        maxS[0] = nums[0]
        maxS[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxS[i] = max(nums[i] + maxS[i - 2], maxS[i - 1])

        return maxS[-1]


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
