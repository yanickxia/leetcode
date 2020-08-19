class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0 for x in range(n + 1)]
        dp[0] = 0
        if n >= 1:
            dp[1] = 10
        if n >= 2:
            dp[2] = 9 * 9
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)
        return sum(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(4))
    print(s.countNumbersWithUniqueDigits(0))
    print(s.countNumbersWithUniqueDigits(1))
    print(s.countNumbersWithUniqueDigits(2))
    print(s.countNumbersWithUniqueDigits(3))
