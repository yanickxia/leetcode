# -*- coding:utf-8 -*-

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start_index, end_index, sum_range, max_end_index = 0, 0, nums[0], -1
        rs = []
        count_rs = len(rs)
        while start_index < len(nums) :
            rs = self.find_from_start_end_index_rs(nums, k, start_index)
            count_rs += len(rs)
            start_index += 1

        return count_rs

    def find_from_start_end_index_rs(self, nums, k, from_index):
        end_index, sum_range = from_index, nums[from_index]
        rs = []
        if nums[from_index] == k:
            rs.append((from_index, end_index))
        while end_index < len(nums) - 1:
            end_index += 1
            sum_range += nums[end_index]
            if sum_range == k:
                rs.append((from_index, end_index))
        return rs


s = Solution()
print(s.subarraySum([1, 2, 3], 3))
# print(s.subarraySum([1, 1, 1], 2))
# print(s.subarraySum([100, 1, 2, 3, 4], 6))
# print(s.subarraySum([-1, -1, 1], 0))
