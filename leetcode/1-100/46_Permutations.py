# -*- coding:utf-8 -*-

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        permute_rs = []
        for i in range(0, len(nums)):
            new_nums = list(nums)
            del new_nums[i]
            rs = self.permute(new_nums)
            for x in rs:
                t = [nums[i]]
                t.extend(x)
                permute_rs.append(t)

        return permute_rs


s = Solution()
print(s.permute([1, 2, 3]))
