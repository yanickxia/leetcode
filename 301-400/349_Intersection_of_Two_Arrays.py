# -*- coding:utf-8 -*-

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set([i for i in nums1 if i in nums2]))


if __name__ == '__main__':
    print Solution().intersection([1, 2, 2, 1], [2, 2])
