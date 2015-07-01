__author__ = 'Yann'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        nums = sorted(nums)

        if len(nums) == 1:
            return nums[0]

        i = 0
        while i < len(nums):

            if i == len(nums) - 1:
                return nums[i]

            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]


s = Solution()

print(s.singleNumber([1, 0, 1]))
