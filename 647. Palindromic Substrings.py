# -*- coding:utf-8 -*-

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = [[True] * len(s)] + [[False for x in range(len(s))] for x in range((len(s) - 1))]
        count = len(s)
        for i in range(1, len(s)):
            for j in range(i, len(s)):
                a = s[j]
                b = s[j - i]
                rs[i][j] = a == b and (rs[i - 2][j - 1] or i < 2)
                if rs[i][j]:
                    count += 1
        return count


s = Solution()
print(s.countSubstrings("aaa"))
print(s.countSubstrings("abc"))
