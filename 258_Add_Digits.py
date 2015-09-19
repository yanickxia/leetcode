__author__ = 'Yann.Xia'


class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0

        r = num % 9
        if r == 0:
            r = 9
        return r

### TRY


s = Solution()

for i in range(1, 100):
    print(s.addDigits(i))
