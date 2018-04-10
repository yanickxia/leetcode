# -*- coding:utf-8 -*-

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '(' + str(self.start) + ' ' + str(self.end) + ')'


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        rs = []
        for i in range(0, len(intervals)):
            x, intervals = self.one_way_merge(intervals[i:])
            rs.append(x)

        return rs

    def one_way_merge(self, intervals):
        if len(intervals) == 1:
            return intervals[0]

        temp = intervals[0]
        rs = []
        for x in intervals[1:]:
            t = self.merge_two(temp, x)
            if t is not None:
                temp = x
            else:
                rs.append(x)
        return temp, rs

    def merge_two(self, interval_a, interval_b):
        if interval_a.end < interval_b.start or interval_a.start > interval_b.end:
            return None
        else:
            return Interval(min(interval_a.start, interval_b.start), max(interval_a.end, interval_b.end))


s = Solution()
print(s.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))
print(s.merge([Interval(0, 0), Interval(1, 4)]))
