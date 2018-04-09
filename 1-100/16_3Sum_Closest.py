# -*- coding:utf-8 -*-

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mindiff = 100000
        res = 0
        for i in range(len(nums)):
            left = i + 1;
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < mindiff: mindiff = diff; res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return res

    def findCloestZ(self, nums, start, z):
        clost_j = start + 1
        for i in range(start + 1, len(nums)):
            if abs(nums[i] - z) < abs(nums[clost_j] - z):
                clost_j = i

        return nums[clost_j]


s = Solution()
print s.threeSumClosest([0, 1, 2], 0)
print s.threeSumClosest([0, 2, 1, -3], 1)
print s.threeSumClosest([1, 1, 1, 0], -100)
print s.threeSumClosest([-1, 2, 1, -4], 1)
