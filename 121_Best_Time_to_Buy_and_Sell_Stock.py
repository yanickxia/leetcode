__author__ = 'Yann.Xia'


class Solution:
    # \@param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):

        if prices == []:
            return 0

        min_point = prices[0]
        max_profit = 0
        for i in range(0, len(prices)):
            if min_point > prices[i]:
                min_point = prices[i]

            profit = prices[i] - min_point
            if profit > max_profit:
                max_profit = profit

        return max_profit


s = Solution()
print(s.maxProfit([4, 1, 2]))
print(s.maxProfit([2, 4, 1]))
print(s.maxProfit([7, 2, 4, 1]))
