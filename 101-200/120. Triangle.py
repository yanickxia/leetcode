from typing import List
import copy


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = copy.deepcopy(triangle)
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j - 1 >= 0 and j < len(triangle[i - 1]):
                    dp[i][j] = min(dp[i - 1][j - 1] + triangle[i][j], dp[i - 1][j] + triangle[i][j])
                elif j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]

        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
