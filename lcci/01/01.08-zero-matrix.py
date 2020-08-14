from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in row_set:
            for j in range(n):
                matrix[i][j] = 0

        for j in col_set:
            for i in range(m):
                matrix[i][j] = 0

if __name__ == '__main__':
    s = Solution()
    rs = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    s.setZeroes(rs)
    print(rs)
