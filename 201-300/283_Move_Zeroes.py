__author__ = 'Yann.Xia'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 1:
            return
        i = 0
        j = len(nums)
        k = 0

        while i != j:
            n_i = nums[i]
            if n_i == 0:
                i += 1
                continue

            nums[i] = 0
            nums[k] = n_i

            k += 1
            i += 1



s = Solution()

lst = [1, 0]
s.moveZeroes(lst)

print(lst)