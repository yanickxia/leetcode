# -*- coding:utf-8 -*-


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n = n / 5
            res += n
        return res



if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(3)
    print s.trailingZeroes(5)
    print s.trailingZeroes(50)
    print s.trailingZeroes(6164)
