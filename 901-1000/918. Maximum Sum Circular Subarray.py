from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums):
        preMax = preMin = maxAns = minAns = 0
        if max(nums) <= 0:
            return max(nums)
        for i in nums:
            preMax = max(i, preMax + i)
            preMin = min(i, preMin + i)
            maxAns = max(maxAns, preMax)
            minAns = min(minAns, preMin)
        return max(maxAns, sum(nums) - minAns)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))
