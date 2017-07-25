class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        max_len = len(nums)

        if k != 0:
            nums = [x % k for x in nums]

        for i in range(2, max_len + 1):
            for j in range(0, max_len - i + 1):
                sum_d = sum(nums[j:j + i])
                if sum_d == 0:
                    return True

                if sum_d == k:
                    return True

        return False


s = Solution()

print s.checkSubarraySum([23, 2, 4, 6, 7], 6)
print s.checkSubarraySum([23, 2, 4, 6, 7], -6)
print s.checkSubarraySum([0, 0], 0)
