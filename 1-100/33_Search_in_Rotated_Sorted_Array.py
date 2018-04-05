# -*- coding:utf-8 -*-

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        pivot_num, pivot_num_index = None, None
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot_num, pivot_num_index = nums[i], i
                break

        left_nums = nums[0:pivot_num_index]
        right_nums = nums[pivot_num_index:]

        if pivot_num_index is None:
            pivot_num_index = 0

        if nums[pivot_num_index - 1] >= target >= nums[0]:
            x = Solution.binary_search_loop(left_nums, target)
            if x is not None:
                return x
            return -1
        else:
            x = Solution.binary_search_loop(right_nums, target)
            if x is not None:
                return x + pivot_num_index
            return -1

    @staticmethod
    def binary_search_loop(lst, value):
        if lst is []:
            return -1

        low, high = 0, len(lst) - 1

        while low <= high:
            mid = (low + high) / 2
            if lst[mid] < value:
                low = mid + 1
            elif lst[mid] > value:
                high = mid - 1
            else:
                return mid
        return None


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([5, 1, 3], 3))
print(s.search([1], 1))
print(s.search([3, 1], 3))
print(s.search([], 5))
