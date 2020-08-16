from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for x in range(n):
                        if matrix[x][j] != -1 and matrix[x][j] != 0:
                            matrix[x][j] = -1
                    for y in range(m):
                        if matrix[i][y] != -1 and matrix[i][y] != 0:
                            matrix[i][y] = -1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        print(matrix)



if __name__ == '__main__':
    s = Solution()
    s.setZeroes([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ])
