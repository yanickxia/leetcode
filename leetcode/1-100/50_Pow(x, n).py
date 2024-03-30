# -*- coding:utf-8 -*-

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        if n == 1:
            return x

        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, (n - 1) / 2)


s = Solution()
print(s.myPow(2.0, 10))
print(s.myPow(2.1, 3))
print(s.myPow(34.00515, -3))
