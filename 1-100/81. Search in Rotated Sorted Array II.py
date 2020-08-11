from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        rotated = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                rotated = i

        return target in nums[0:rotated] or target in nums[rotated:]


if __name__ == '__main__':
    s = Solution()
    print(s.search([1], 1))
