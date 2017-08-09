# -*- coding:utf-8 -*-
from unittest import TestCase


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        top_line, bottom_line, direction = 0, numRows - 1, True  # if direction = True to down or Up
        rs = [''] * numRows
        n = 0
        for s_i in s:
            rs[n] += (s_i)
            n, direction = self.get_next_line(n, numRows, direction)

        return ''.join(rs)

    def get_next_line(self, n, numRow, direction):
        if direction and n < numRow - 1:
            return (n + 1, direction)
        if direction and n == numRow - 1:
            return (n - 1, not direction)
        if not direction and n > 0:
            return (n - 1, direction)
        return (n + 1, not direction)


class SolutionTest(TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
