from typing import List


# 肯定又是 DP
# dp[i][j]:  从 i 到 j 的最小次数


class Solution(object):
    def jump(self, nums):
        if not nums or len(nums) ==1:
            return 0
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i):
                if i <= j + nums[j]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 0, 1, 4]) == 2)
    print(s.jump([2, 3, 1, 1, 4]) == 2)
    print(s.jump([]) == 0)
    print(s.jump([2]) == 0)
    print(s.jump([2, 1]) == 1)
    print(s.jump([2, 1, 1]) == 1)
