# -*- coding:utf-8 -*-

class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in range(1, n):
            s = self.cal(s)
        return s

    def cal(self, s):
        cnt = 1
        length = len(s)
        ans = ''
        for i, c in enumerate(s):
            if i + 1 < length and s[i] != s[i + 1]:
                ans = ans + str(cnt) + c
                cnt = 1
            elif i + 1 < length:
                cnt = cnt + 1

        ans = ans + str(cnt) + c
        return ans
