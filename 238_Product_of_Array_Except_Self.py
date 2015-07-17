__author__ = 'Yann'


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        size = len(nums)
        output = [1] * size
        left = 1

        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left
        right = 1

        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output


s = Solution()

print(s.productExceptSelf([1, 2, 3, 4]))
