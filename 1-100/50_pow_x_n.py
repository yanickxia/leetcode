# -*- coding:utf-8 -*-
import math


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        rs = x
        is_negative = False
        if n < 0:
            is_negative = True

        if x == 1:
            return 1

        if n == 0:
            return 1
        if n == 1:
            return float(('%.5f' % rs))

        n = abs(n)

        rs, n = self.mul_by_n(x, n)
        real_rs = rs
        while n > 0:
            t_rs, n = self.mul_by_n(x, n)
            real_rs *= t_rs

        if is_negative:
            real_rs = 1 / real_rs
        return float(('%.5f' % real_rs))

    def mul_by_n(self, rs, n):
        if n == 1:
            return rs, 0
        source_n, c = n, 0

        while n > 1:
            if rs == 0:
                return (0, 0)
            rs = rs * rs
            rs = float(('%.20f' % rs))
            n = int(math.sqrt(n))
            c += 1
        return rs, source_n - 2 ** c


s = Solution()
print(s.myPow(2.00000, 10))
# print(s.myPow(34.00515, -3))
# print(s.myPow(-2, 2))
# print(s.myPow(0.00001, 2147483647))
# print(s.myPow(0.25519, -6))  # 3620.91299
# print(s.myPow(0.99999, 948688))
# print(s.myPow(-0.99999, 933520))
print(s.myPow(-0.99999, 933520))
print(s.myPow(1.00000,
              2147483647))
