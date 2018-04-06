# -*- coding:utf-8 -*-

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        permute_rs = []
        for i in set(nums):
            new_nums = list(nums)
            new_nums.remove(i)
            rs = self.permuteUnique(new_nums)
            for x in rs:
                t = [i]
                t.extend(x)
                permute_rs.append(t)

        return permute_rs


s = Solution()
print(s.permuteUnique([1, 1, 2]))
