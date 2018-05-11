# -*- coding:utf-8 -*-
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        rs = []
        rs.append([1, 1])
        if rowIndex == 1:
            return rs[-1]

        i = rowIndex - 1
        while i > 0:
            latest_nums = rs[-1]
            ts = []
            for j in range(0, len(latest_nums) - 1):
                ts.append(latest_nums[j] + latest_nums[j + 1])
            ts = [1] + ts + [1]
            rs.append(ts)
            i -= 1
        return rs[-1]


s = Solution()
print(s.getRow(3))
