# -*- coding:utf-8 -*-


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i, len_nums = 0, len(nums)
        while i != len_nums:
            if nums[i] == val:
                del nums[i]
                len_nums = len(nums)
            else:
                i += 1
        return len_nums

s = Solution()
print s.removeElement([3, 2, 2, 3], 3)
