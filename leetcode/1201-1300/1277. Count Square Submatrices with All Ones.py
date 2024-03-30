from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mn = min(m, n)

        def is_squares(matrix: List[List[int]], i, j, k):
            m = len(matrix)
            n = len(matrix[0])
            if i + k > m:
                return False
            if j + k > n:
                return False

            for row in range(i, i + k):
                for col in range(j, j + k):
                    if matrix[row][col] != 1:
                        return False
            return True

        def clean(matrix: List[List[int]], i, j, k):
            for row in range(i, i + k):
                for col in range(j, j + k):
                    matrix[row][col] = 0

        found_squares = [0 for i in range(mn + 1)]
        for i in range(m):
            for j in range(n):
                # found maxium square
                if matrix[i][j] == 1:
                    k = 1
                    while k <= mn:
                        if is_squares(matrix, i, j, k):
                            k += 1
                            found_squares[k - 1] += 1
                        else:
                            break

                    #clean(matrix, i, j, k - 1)
                    #found_squares[k - 1] += 1

        return sum(found_squares)


if __name__ == '__main__':
    s = Solution()
    print(s.countSquares([[1, 0, 1, 0, 1],
                          [1, 0, 0, 1, 1],
                          [0, 1, 0, 1, 1],
                          [1, 0, 0, 1, 1]]))

    print(s.countSquares([[0, 0, 0],
                          [0, 1, 0],
                          [0, 1, 0],
                          [1, 1, 1],
                          [1, 1, 0]])
          )

    print(s.countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))
    print(s.countSquares([
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]))
