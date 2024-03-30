# -*- coding:utf-8 -*-

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        return max([min(i + 1, c) for i, c in enumerate(citations[::-1])])


if __name__ == '__main__':
    print [0,1,3,5,6]
    print [0,1,3,5,6][::-1]