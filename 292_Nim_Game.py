__author__ = 'yann'


class Solution(object):
    def canWinNim(self, n):
        if n % 4 == 0:
            return False
        return True


s = Solution()

print(s.canWinNim(0))