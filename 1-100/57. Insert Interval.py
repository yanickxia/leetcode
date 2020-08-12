from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        m = max([x[1] for x in intervals])
        marked = [None for x in range(m + 1)]
        for interval in intervals:
            begin = interval[0]
            end = interval[1]

            # LR
            if begin == end:
                if not marked[begin]:
                    marked[begin] = "LR"
                continue

            if marked[begin] == 'R':
                marked[begin] = 'C'

            if not marked[begin]:
                marked[begin] = 'L'


            if marked[end] == 'L':
                marked[end] = 'C'

            if not marked[end]:
                marked[end] = 'R'

            begin += 1
            while begin != end:
                marked[begin] = 'C'
                begin +=1


        i = 0
        new_intervals = []
        while i < m:
            if marked[i] == 'LR':
                new_intervals.append([i,i])

            if marked[i] == 'L':
                j = i+1
                while marked[j] != 'R':
                    j+=1
                new_intervals.append([i,j])
                i = j
            i+=1



        return new_intervals


# [[1,2],[3,10],[12,16]]

if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1, 5], [10, 11], [15, 2147483647]], [5, 7]))
    print(s.insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]])
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
    print(s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
    print(s.insert([[1, 5]], [1, 7]) == [[1, 7]])


