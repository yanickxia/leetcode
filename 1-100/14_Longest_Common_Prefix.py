# -*- coding:utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        row, column, row_size, column_size, comm_str = 0, 0, len(min(strs)), len(strs), ""

        for row in xrange(0, row_size, 1):
            for column in xrange(1, column_size, 1):
                if strs[column - 1][row] != strs[column][row]:
                    return comm_str
            comm_str += strs[0][row]

        return comm_str

s = Solution()
print s.longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"])
print s.longestCommonPrefix(["flower","flow","flight"])
