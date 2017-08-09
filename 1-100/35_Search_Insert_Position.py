__author__ = 'yann'


class Solution(object):
    def searchInsert(self, nums, target):
        count = 0
        for n in nums:
            if target <= n:
                return count
            count += 1
        return count

s = Solution()
print(s.searchInsert([1,3,5,6], 5))
