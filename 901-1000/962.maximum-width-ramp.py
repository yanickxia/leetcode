#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        i = n - 1
        ans = 0
        while i >= 0:
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans


# @lc code=end

s = Solution()
print(s.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
