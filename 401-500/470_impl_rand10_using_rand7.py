# -*- coding:utf-8 -*-


# The rand7() API is already defined for you.
import random


def rand7():
    return random.randint(1, 7)


# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        matrix = [[1, 2, 3, 4, 5, 6, 7],
                  [8, 9, 10, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9, 10, 1],
                  [2, 3, 4, 5, 6, 7, 8],
                  [9, 10, 1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10, 0, 0],  # Last 2 elements are invalid
                  [0, 0, 0, 0, 0, 0, 0]]  # Entire row is invalid
        while True:
            row = rand7() - 1
            col = rand7() - 1
            if row == 5 and col >= 5:
                continue
            elif row == 6:
                continue
            return matrix[row][col]


if __name__ == '__main__':
    s = Solution()
    print s.rand10()
