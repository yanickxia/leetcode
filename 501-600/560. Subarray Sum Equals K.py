# -*- coding:utf-8 -*-

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a_sum, result = 0, 0
        preSum = {}
        preSum[0] = 1

        for i in range(0, len(nums)):
            a_sum += nums[i]
            if preSum.get(a_sum - k) is not None:
                result += preSum.get(a_sum - k)
            if preSum.get(a_sum) is None:
                x = 1
            else:
                x = preSum.get(a_sum) + 1
            preSum[a_sum] = x
        return result


s = Solution()
print(s.subarraySum([1, 2, 3], 3))
# print(s.subarraySum([1, 1, 1], 2))
# print(s.subarraySum([100, 1, 2, 3, 4], 6))
# print(s.subarraySum([-1, -1, 1], 0))
