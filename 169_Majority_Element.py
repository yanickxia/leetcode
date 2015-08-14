__author__ = 'yann'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums = sorted(nums)
        return nums[len(nums)/2]

s = Solution()
print(s.majorityElement([1,2,5,6,3,10,2,3,4,1,1]))