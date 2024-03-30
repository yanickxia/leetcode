# -*- coding:utf-8 -*-

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        found_index = Solution.binary_search_loop(nums, target)
        if found_index is None:
            return [-1, -1]
        left_index = found_index
        right_index = found_index

        while left_index >= 0:
            if nums[left_index] == nums[found_index]:
                left_index -= 1
            else:
                break
        while right_index < len(nums):
            if nums[right_index] == nums[found_index]:
                right_index += 1
            else:
                break

        return [left_index + 1, right_index - 1]

    @staticmethod
    def binary_search_loop(lst, value):
        if len(lst) == 0:
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
print(s.searchRange([1], 1))
print(s.searchRange([], 0))
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([1], 0))
