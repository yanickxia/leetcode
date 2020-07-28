from typing import List

'''
i is begin index, j is end index                 
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([]))
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
    print(s.lengthOfLIS([1, 2, 3, 4]))
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
