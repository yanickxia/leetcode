# -*- coding:utf-8 -*-

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 11))
print(s.coinChange([2, 5, 10, 1], 27))
print(s.coinChange([186, 419, 83, 408], 6249))
print(s.coinChange([130, 129, 400, 289, 230, 135], 8270))
