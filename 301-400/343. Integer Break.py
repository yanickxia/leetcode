
"""
"""





class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        if n > 2:
            dp[3] = 2

        for i in range(4, n+1):
            grest = -1
            for j in range(2, int(i/2)+1):
                n1 = j
                n2 = i - j
                maxP1 = dp[n1] if dp[n1] > n1 else n1
                maxP2 = dp[n2] if dp[n2] > n2 else n2
                maxP = maxP1 * maxP2
                if maxP > grest:
                    grest = maxP
            dp[i] = grest

        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))