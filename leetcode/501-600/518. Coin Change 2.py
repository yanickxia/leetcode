from typing import List


###
### dp[j] = ∑dp[j-coins[i]]
###

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()  # make coins is sorted
        dp = [0] + [0 for i in range(amount)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1, 2, 5]))
