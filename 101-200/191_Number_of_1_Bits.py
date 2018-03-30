__author__ = 'Yann'


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        n = str(bin(n))
        counter = 0
        for x in n:
            if x == '1':
                counter += 1
        return counter



s = Solution()

print(s.hammingWeight(11))