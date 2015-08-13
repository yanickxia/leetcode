__author__ = 'Yann.Xia'


class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        count = [0] * (n + 1)
        count[0], count[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(0, i):
                count[i] += count[j] * count[i - j - 1]

        return count[n]
