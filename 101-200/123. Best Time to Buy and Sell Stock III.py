from typing import List


# local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
# global[i][j] = max(local[i][j], global[i - 1][j])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        loc, glo = [[0 for i in range(3)] for j in range(n)], [[0 for i in range(3)] for j in range(n)]
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(1, 3):
                loc[i][j] = max(glo[i - 1][j - 1] + max(diff, 0), loc[i - 1][j] + diff)
                glo[i][j] = max(loc[i][j], glo[i - 1][j])

        return glo[n - 1][2]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
