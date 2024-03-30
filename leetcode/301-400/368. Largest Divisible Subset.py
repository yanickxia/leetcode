# -*- coding:utf-8 -*-


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        nums = sorted(nums)
        largest_length = [0] * len(nums)
        largest_start = [[]] * len(nums)
        for i in xrange(0, len(nums)):
            largest_start[i] = []

        for i in xrange(0, len(nums)):
            for j in xrange(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and \
                        largest_length[i] + 1 > largest_length[j]:
                    largest_length[j] = largest_length[i] + 1
                    largest_start[j].append(i)

        index = largest_length.index(max(largest_length))
        res = []
        for i in largest_start[index]:
            res.append(nums[i])
        res.append(nums[index])
        return res


if __name__ == '__main__':
    s = Solution()
    print s.largestDivisibleSubset([])
    print s.largestDivisibleSubset([1])
    print s.largestDivisibleSubset([1, 2, 3])
    print s.largestDivisibleSubset([1, 2, 4, 8])
