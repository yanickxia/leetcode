# -*- coding:utf-8 -*-

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        news_n = [0] * len(nums)
        for n in nums:
            if news_n[n - 1] == 0:
                news_n[n - 1] = 1
            else:
                return n


s = Solution()
print(s.findDuplicate([1,1,2,3,4]))
