from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxium, i = 0, 0

        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums) and nums[j] > nums[j - 1]:
                j += 1
            if j - i > maxium:
                maxium = j - i
            i = j
        return maxium


if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(s.findLengthOfLCIS([2, 2, 2, 2, 2, 2]))
    print(s.findLengthOfLCIS([0]))
    print(s.findLengthOfLCIS([1,0]))
