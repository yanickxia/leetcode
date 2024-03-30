# -*- coding:utf-8 -*-

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = {}
        index = []
        for i in xrange(len(s)):
            if rs.get(s[i]) is None:
                rs[s[i]] = [i]
            else:
                rs[s[i]].append(i)

        for key in rs.keys():
            if len(rs[key]) == 1:
                index.append(rs[key][0])
        if len(index) == 0:
            return -1

        return min(index)


s = Solution()
print s.firstUniqChar("leetcode")
