from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        dp[0] = 0
        for i in range(1, (num + 1)):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))