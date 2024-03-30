from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, ans = 0, 0, 0
        while i < len(nums):
            j = i
            product = nums[i]
            tmp = []
            while product < k:
                tmp.append(nums[j])
                j += 1
                if j == len(nums):
                    break
                product *= nums[j]
            print(tmp)
            if j == i:
                i += 1
            else:
                i = j
        return ans


s = Solution()
print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
