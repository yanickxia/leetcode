from unittest import TestCase


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        k = (len(nums1) + len(nums2)) / 2.0
        isPair = False
        if int(k) == k:
            isPair = True
            k -= 1
        return self.findKSortByTwo(nums1, nums2, int(k), isPair)

    def findKSortByTwo(self, nums1, nums2, k, isPair):
        if len(nums1) == 0:
            return self.findKSortByOne(nums2, k, isPair)
        elif len(nums2) == 0:
            return self.findKSortByOne(nums1, k, isPair)

        if k == 0:
            return self.getValue(nums1, nums2, isPair)

        skipN = int(k) / 2
        if skipN > len(nums1):
            skipN = len(nums1)
        elif skipN > len(nums2):
            skipN = len(nums2)
        if skipN == 0:
            skipN = 1

        if nums1[skipN - 1] > nums2[skipN - 1]:
            return self.findKSortByTwo(nums1, nums2[skipN:], k - skipN, isPair)
        else:
            return self.findKSortByTwo(nums1[skipN:], nums2, k - skipN, isPair)

    def findKSortByOne(self, num, k, isPair):
        if isPair:
            return (num[k] + num[k + 1]) / 2.0
        return num[k]

    def getValue(self, nums1, nums2, isPair):
        if isPair:
            lst = sorted(nums1 + nums2)
            return (lst[0] + lst[1]) / 2.0
        else:
            return min(nums1[0], nums2[0])


class SolutionTest(TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.findMedianSortedArrays([1, 2], [1, 1]), 1.0)

        self.assertEqual(s.findMedianSortedArrays([1, 3, 4], [2]), 2.5)

        self.assertEqual(s.findMedianSortedArrays([1], [2, 3, 4, 5, 6, 7, 8]), 4.5)

        self.assertEqual(s.findMedianSortedArrays([], [1, 2]), 1.5)
        self.assertEqual(s.findMedianSortedArrays([1, 2], []), 1.5)
        self.assertEqual(s.findMedianSortedArrays([], [1, 2, 3]), 2)
        self.assertEqual(s.findMedianSortedArrays([1, 2, 3], []), 2)

        self.assertEqual(s.findMedianSortedArrays([1, 3], [2]), 2)

        self.assertEqual(s.findMedianSortedArrays([1, 1, 1], [1, 1, 1]), 1)
        self.assertEqual(s.findMedianSortedArrays([1, 1], [1, 1]), 1)
        self.assertEqual(s.findMedianSortedArrays([3, 4], [1, 2]), 2.5)
