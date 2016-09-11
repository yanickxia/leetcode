from unittest import TestCase


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class SolutionTest(TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
