# -*- coding:utf-8 -*-


from unittest import TestCase


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        size = len(height)
        i = 0
        j = size - 1

        while i < j:
            x = height[i]
            y = height[j]

            area = min(x, y) * (j - i)
            if area > max_area:
                max_area = area

            if x > y:
                j -= 1
            else:
                i += 1

        return max_area


class SolutionTest(TestCase):
    def test(self):
        s = Solution()

        # print s.maxArea([0, 2])
        # print s.maxArea([1, 2])
        # print s.maxArea([1, 1])
        print s.maxArea([2, 3, 4, 5, 18, 17, 6])
        print s.maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4])
