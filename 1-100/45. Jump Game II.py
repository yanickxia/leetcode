from typing import List


# 肯定又是 DP
# dp[i][j]:  从 i 到 j 的最小次数


class Solution(object):
    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = curEnd = maxReach = 0
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, nums[i] + i)
            if i == curEnd:
                jumps += 1
                curEnd = maxReach
        return jumps

    def jump(self, nums):
        step, n, i, cur = 0, len(nums), 0, 0
        while cur < n - 1:
            step += 1
            pre = cur
            for i in range(pre + 1):
                cur = max(cur, i + nums[i])
        return step


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 0, 1, 4]) == 2)
    print(s.jump([2, 3, 1, 1, 4]) == 2)
    print(s.jump([]) == 0)
    print(s.jump([2]) == 0)
    print(s.jump([2, 1]) == 1)
    print(s.jump([2, 1, 1]) == 1)
