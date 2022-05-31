#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res



# @lc code=end
s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
#         n = len(heights)
#         remain = n
#         loop = min(heights)
#         heights = [x - loop + 1 for x in heights]
#
#         ans = 0
#         while remain > 0:
#             i = 0
#             remain = 0
#             while i < n:
#                 if heights[i] != 0:
#                     tmp = 0
#                     while i < n and heights[i] != 0:
#                         tmp += 1
#                         heights[i] -= 1
#                         i += 1
#                     tmp *= loop
#                     ans = max(tmp, ans)
#                     remain += 1
#                 i += 1
#             loop += 1
#         return ans