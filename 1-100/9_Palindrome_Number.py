# -*- coding:utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = x
        z = 0
        while y != 0:
            z = z * 10 + (y % 10)
            y /= 10

        if z == x or z == -x:
            return True
        return False


s = Solution()
print s.isPalindrome(2147447412)
# print s.isPalindrome(121)
# print s.isPalindrome(123)
# print s.isPalindrome(1221)
# print s.isPalindrome(12321)
# print s.isPalindrome(0)
