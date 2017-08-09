# -*- coding:utf-8 -*-

from unittest import TestCase


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        if s is None or s is '' or len(s) < 1:
            return 0

        isNegtive = 1
        number = 0

        while s[0] == ' ':
            s = s[1:]
            if len(s) < 1:
                return number

        if s[0] == '-' or s[0] == '+':
            if s[0] == "-":
                isNegtive = -1
            s = s[1:]

        if len(s) == 0:
            return number
        if s[0] == '+' or s[0] == '-':
            return 0

        # space 0
        while s[0] == '0':
            s = s[1:]

        while len(s) > 0:
            n = self.getNumber(s[0])
            if n == -1:
                return self.returnNumber(isNegtive * number)
            number = number * 10 + n
            s = s[1:]

        return self.returnNumber(isNegtive * number)

    def returnNumber(self, n):
        if n >= 2147483647:
            return 2147483647
        elif n <= -2147483648:
            return -2147483648
        return n

    def getNumber(self, nStr):
        if nStr == '0':
            return 0
        elif nStr == '1':
            return 1
        elif nStr == '2':
            return 2
        elif nStr == '3':
            return 3
        elif nStr == '4':
            return 4
        elif nStr == '5':
            return 5
        elif nStr == '6':
            return 6
        elif nStr == '7':
            return 7
        elif nStr == '8':
            return 8
        elif nStr == '9':
            return 9
        else:
            return -1


class SolutionTest(TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.myAtoi("2147483648"), 2147483647)
        self.assertEqual(s.myAtoi("  -0012a42"), -12)
        self.assertEqual(s.myAtoi("  -0012a42"), -12)
        self.assertEqual(s.myAtoi("  -0012a42"), -12)
        self.assertEqual(s.myAtoi("  -0012a42"), -12)
        self.assertEqual(s.myAtoi("  -0012a42"), -12)

        self.assertEqual(s.myAtoi("  -0012a42"), -12)
        self.assertEqual(s.myAtoi("+-2"), 0)
        self.assertEqual(s.myAtoi("-1"), -1)
        self.assertEqual(s.myAtoi("    010"), 10)
        self.assertEqual(s.myAtoi("-"), 0)
        self.assertEqual(s.myAtoi("+"), 0)
        self.assertEqual(s.myAtoi(""), 0)
        self.assertEqual(s.myAtoi('111'), 111)
