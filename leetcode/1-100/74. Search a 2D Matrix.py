from typing import List


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False



if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1],[3],[5]],5))

    print(s.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3))
    print(s.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 13))
    print(s.searchMatrix([],1))
    print(s.searchMatrix([[]], 1))
    print(s.searchMatrix([
        [1, 3, 5, 7]
    ], 1))
    print(s.searchMatrix([[1]],0))
