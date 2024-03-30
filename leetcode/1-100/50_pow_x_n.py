# -*- coding:utf-8 -*-
import math


class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x * x, n / 2) * x
        else:
            return self.myPow(x * x, n / 2)


s = Solution()
print(s.myPow(2.00000, 10))
print(s.myPow(34.00515, -3))
print(s.myPow(-2, 2))
print(s.myPow(0.00001, 2147483647))
print(s.myPow(0.25519, -6))  # 3620.91299
print(s.myPow(0.99999, 948688))
print(s.myPow(-0.99999, 933520))
print(s.myPow(-0.99999, 933520))
print(s.myPow(1.00000, 2147483647))
