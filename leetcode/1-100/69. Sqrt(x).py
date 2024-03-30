# -*- coding:utf-8 -*-
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 二分查找
        if x < 2:
            return x
        low, high = 1, x / 2
        last = 0
        while low <= high:
            mid = (low + high) / 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
                last = mid
            else:
                return mid
        return last


s = Solution()
print(s.mySqrt(1))
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(6))
