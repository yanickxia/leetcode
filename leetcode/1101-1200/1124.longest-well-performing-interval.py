#
# @lc app=leetcode id=1124 lang=python3
#
# [1124] Longest Well-Performing Interval
#

# @lc code=start
from typing import List


# f(i,j) = max(f(i,j-1), f(i+1,j))


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if x > 8 else -1 for x in hours]
        prefixSum = []
        cur_sum = 0
        for val in hours:
            prefixSum.append(cur_sum)
            cur_sum += val
        prefixSum.append(cur_sum)

        ans = 0
        stack = []
        for i in range(len(hours)+1):
            if not stack or prefixSum[stack[-1]] > prefixSum[i]:
                stack.append(i)
        # 这里的栈代表的是 (i,j) 对的底部
        i = len(hours)
        while i > ans:
            while stack and prefixSum[stack[-1]] < prefixSum[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
            i -= 1
        return ans

# @lc code=end
s = Solution()
print(s.longestWPI([9,9,6,0,6,6,9]))
