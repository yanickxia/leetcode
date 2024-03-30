#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from operator import ne


class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            if n == 1:
                return True
            if n == 7:
                return True
            return False
        next = 0
        while n > 0:
            x = n % 10
            next += x * x
            n = (n - x) / 10 
        return self.isHappy(next)
# @lc code=end

