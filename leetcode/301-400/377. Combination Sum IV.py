from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()  # make coins is sorted
        dp = [0] + [0 for i in range(target)]
        dp[0] = 1


        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i - n]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
