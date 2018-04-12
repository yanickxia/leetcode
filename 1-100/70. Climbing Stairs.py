# -*- coding:utf-8 -*-

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """


        if n == 1:
            return 1
        if n == 2:
            return 2

        x = [1, 2]
        x.extend([0] * (n - 2))

        for i in xrange(2, n):
            x[i] = x[i-1]+x[i-2]

        return x[-1]


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(35))
