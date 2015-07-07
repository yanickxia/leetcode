__author__ = 'Yann.Xia'


class Solution:
    # \@param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):

        if prices == [] or len(prices) == 1:
            return 0

        diff_prices = []

        for i in range(1, len(prices)):
            diff_prices.append(prices[i] - prices[i - 1])

        profile = 0
        for diff in diff_prices:
            if diff > 0:
                profile += diff

        return profile


s = Solution()
print(s.maxProfit([4, 1, 2]))
print(s.maxProfit([2, 4, 1]))
print(s.maxProfit([7, 2, 4, 1]))
