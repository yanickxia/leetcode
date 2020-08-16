from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            intervals = [newInterval] + intervals
            return intervals

        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        if newInterval[0] <= intervals[0][0] and newInterval[1] >= intervals[-1][1]:
            return [newInterval]

        def in_interval(inter, num):
            return inter[0] <= num <= inter[1]

        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                intervals.insert(i, newInterval)
                return intervals
            if in_interval(interval, newInterval[0]) and in_interval(interval, newInterval[1]):
                return intervals
            if newInterval[0] < interval[0] and newInterval[1] <= interval[1]:
                return intervals[:i] + [[newInterval[0], interval[1]]] + intervals[i + 1:]

            if in_interval(interval, newInterval[0]) or newInterval[0] < interval[0]:
                found_in_gap, j = True, i
                new_begin = min(newInterval[0] , interval[0] ) if newInterval[0] < interval[0]  else interval[0]
                while True:
                    if found_in_gap:
                        if j == len(intervals) - 1:
                            return intervals[:i] + [[new_begin, max(newInterval[1], intervals[-1][1])]]

                        gap_l = intervals[j][1]
                        gal_r = intervals[j + 1][0]
                        if newInterval[1] < gal_r:
                            return intervals[:i] + [[new_begin, newInterval[1]]] + intervals[j + 1:]
                        found_in_gap = not found_in_gap
                        j += 1
                    else:
                        if in_interval(intervals[j], newInterval[1]):
                            return intervals[:i] + [[new_begin, intervals[j][1]]] + intervals[j + 1:]
                        found_in_gap = not found_in_gap

            i += 1

        return intervals


# [[1,2],[3,10],[12,16]]

if __name__ == '__main__':
    s = Solution()
    print(s.insert([[0, 5], [9, 12]], [7, 16]) == [[0, 5], [7, 16]])
    print(s.insert([[1, 5]], [0, 6]) == [[0, 6]])
    print(s.insert([[1, 5]], [0, 3]) == [[0, 5]])
    print(s.insert([], [5, 7]) == [[5, 7]])
    print(s.insert([[1, 5]], [1, 7]) == [[1, 7]])
    print(s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
    print(s.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]])
    print(s.insert([[1, 5], [10, 11], [15, 2147483647]], [5, 7]) == [[1, 7], [10, 11], [15, 2147483647]])
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
