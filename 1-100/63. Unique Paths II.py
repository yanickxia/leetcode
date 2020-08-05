from typing import List


# 看起来就像DP

# DP[i][j] = DP[i][j-1] + DP[i-1][j]
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        pos = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] != 1:
                pos[i][0] = 1
            else:
                break

        for i in range(n):
            if obstacleGrid[0][i] != 1:
                pos[0][i] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    pos[i][j] = 0
                    continue

                else:
                    pos[i][j] = pos[i - 1][j] + pos[i][j - 1]

        return pos[-1][-1]


if __name__ == '__main__':
    s = Solution()

    # print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
    # print(s.uniquePathsWithObstacles([
    #     [1, 0]
    # ]))
    print(s.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
