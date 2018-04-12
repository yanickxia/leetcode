# -*- coding:utf-8 -*-

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        start, end = 0, len(nums) - 1
        last = False
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                self.swap(nums, i, start)
                start += 1
                i += 1
            elif nums[i] == 2:
                while nums[end] == 2 and end > 1:
                    end -= 1
                if i > end:
                    return nums
                self.swap(nums, i, end)
                end -= 1
            else:
                i += 1

            if i > end:
                return nums


    def swap(self, nums, i, j):
        x = nums[i]
        nums[i] = nums[j]
        nums[j] = x


s = Solution()
print(s.sortColors([0, 1, 2]))
# s.sortColors([0, 2, 1, 2, 1, 2, 0])

s.sortColors([1, 0])
