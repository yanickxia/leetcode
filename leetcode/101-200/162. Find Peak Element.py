from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        found = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                j = 1
                while i + j + 1 < len(nums) and nums[i + j] < nums[i + j + 1]:
                    j += 1
                found = i + j
                return found
            i += 1
        return found


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([2, 1]))
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
