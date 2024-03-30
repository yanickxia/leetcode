# -*- coding:utf-8 -*-

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        z = K
        res = ""
        for i in xrange(len(S) - 1, -1, -1):
            if z == 0:
                res = "-" + res
                z = K

            if z != 0 and S[i] != '-':
                res = S[i].upper() + res
                z -= 1

        if len(res) > 0 and res[0] == "-":
            return res[1:]

        return res


if __name__ == '__main__':
    s = Solution()
    print s.licenseKeyFormatting("5F3Z-2e-9-w", 4)
    print s.licenseKeyFormatting("2-5g-3-J", 2)
    print s.licenseKeyFormatting("r", 1)
    print s.licenseKeyFormatting("---", 3)
