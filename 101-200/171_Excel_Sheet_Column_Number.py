__author__ = 'Yann'


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        n = 0
        for s_s in s:
            if n != 0:
                n *= 26
            n += self.charToNumber(s_s)
        return n

    def charToNumber(self, c):
        return ord(c) - 64


print(Solution().titleToNumber('AAA'))
