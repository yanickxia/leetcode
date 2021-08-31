from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        m = max(nums)
        n = min(nums)
        maxLen = 0
        i = n
        while i <= m:
            if i in nums:
                j = 0
                while i + j <= m and i + j in nums:
                    j += 1
                if j > maxLen:
                    maxLen = j
                    if maxLen > len(nums) / 2:
                        return maxLen
                i += j
            else:
                i += 1

        return maxLen


if __name__ == '__main__':
    s = Solution()

    print(s.longestConsecutive([0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999]))
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
