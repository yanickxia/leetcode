# -*- coding:utf-8 -*-

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        start, end = 0, len(nums) - 1
        while nums[start] == sort_nums[start] and start < end:
            start += 1
        while nums[end] == sort_nums[end] and end >= start:
            end -= 1

        return end - start + 1


s = Solution()
print(s.findUnsortedSubarray([1, 2, 3, 4]))
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
