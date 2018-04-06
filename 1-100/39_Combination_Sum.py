# -*- coding:utf-8 -*-

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        rs = []
        if target in candidates:
            rs.append([target])

        less_than_target = [x for x in candidates if x < target]
        if len(less_than_target) == 0:
            return []

        for x in less_than_target:
            xr = self.combinationSum(less_than_target, target - x)
            for one_xr in xr:
                temp = [x]
                temp.extend(one_xr)
                rs.append(temp)

        return rs


s = Solution()
print(s.combinationSum([1], 1))
print(s.combinationSum([2, 3, 6, 7], 7))
