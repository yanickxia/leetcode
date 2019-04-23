# -*- coding:utf-8 -*-

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        return max([min(i + 1, c) for i, c in enumerate(sorted(citations, reverse=True))])