# -*- coding:utf-8 -*-

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        resultCodeList = []
        for i in range(0, 2 ** n):
            grayCode = (i >> 1) ^ i
            resultCodeList.append(grayCode)
        return resultCodeList
