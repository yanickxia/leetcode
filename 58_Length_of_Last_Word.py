# -*- coding:utf-8 -*-


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split()) - 1]) if s.split() != [] else 0


print Solution().lengthOfLastWord("Hello World")
