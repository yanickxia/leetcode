# -*- coding:utf-8 -*-

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_count = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == "1":
                    x = self.maximal_square(matrix, i, j)
                    if x > max_count:
                        print(i,j)
                        max_count = x

        return max_count

    def maximal_square(self, matrix, i, j):
        start_i, start_j = i, j
        is_over = True
        while is_over and start_i < len(matrix) - 1 and start_j < len(matrix[start_i]) - 1:
            start_j += 1
            start_i += 1
            for index_i in range(i, start_i + 1):
                for index_j in range(j, start_j + 1):
                    if matrix[index_i][index_j] != '1':
                        return (start_i - i) * (start_i - i)

        return (start_i - i + 1) * (start_i - i + 1)


s = Solution()

print(s.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]))

print(s.maximalSquare(
    [["1", "1"],
     ["1", "1"]]))

print(s.maximalSquare(
    [["1"]]))


