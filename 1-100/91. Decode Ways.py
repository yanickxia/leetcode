class Solution:
    def numDecodings(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if self.isChar(s[0]):
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(2, len(s) + 1):
            if self.isChar(s[i - 1: i]):
                dp[i] += dp[i - 1]
            if self.isChar(s[i - 2: i]):
                dp[i] += dp[i - 2]
        return dp[len(s)]

    def isChar(self, s):
        if s[0] == '0':
            return False
        return int(s) > 0 and int(s) < 27


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("0"))
