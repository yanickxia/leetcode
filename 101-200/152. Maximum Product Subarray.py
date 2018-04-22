class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prodcut = [0] * len(nums)
        min_product = [0] * len(nums)
        max_prodcut[0] = nums[0]
        min_product[0] = nums[0]

        for i in range(1, len(nums)):
            max_prodcut[i] = max(max_prodcut[i - 1] * nums[i], min_product[i - 1] * nums[i], nums[i])
            min_product[i] = min(max_prodcut[i - 1] * nums[i], min_product[i - 1] * nums[i], nums[i])

        return max(max_prodcut)


s = Solution()
print(s.maxProduct([0, 0, 2, 2, 0, 0, 0, 2]))
print(s.maxProduct([0, 0, 2]))
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([0, 2]))
print(s.maxProduct([1, 1, 2, 3, 6]))
print(s.maxProduct([-2]))
print(s.maxProduct([-2, -2]))

print(s.maxProduct([2, -5, -2, -4, 3]))
print(s.maxProduct([3, -1, 4]))
