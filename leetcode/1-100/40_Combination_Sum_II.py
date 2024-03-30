# -*- coding:utf-8 -*-

class Solution(object):
    def combinationSum2(self, candidates, target):
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
            return rs

        for x in set(less_than_target):
            less_than_target_and_bigger_than_x = [y for y in less_than_target if y >= x]
            less_than_target_and_bigger_than_x.remove(x)
            xr = self.combinationSum2(less_than_target_and_bigger_than_x, target - x)
            for one_xr in xr:
                temp = [x]
                temp.extend(one_xr)
                rs.append(temp)

        return rs


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
