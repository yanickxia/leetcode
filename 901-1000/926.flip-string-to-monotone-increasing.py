#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.zeros = []
        self.ones = []
    def minFlipsMonoIncr(self, s: str) -> int:
        self.zeros = []
        zero = 0
        one = 0
        for i in range(0, len(s)):
            if s[i] == '0':
                zero += 1
            self.zeros.append(zero)
        for i in range(len(s)-1, -1,-1):
            if s[i] != '1':
               one += 1
            self.ones.append(one)
        self.ones.reverse()
        self.ones.append(0)


        minFip = float('inf')
        for i in range(0,len(s)):
            # i to zero , after to one
            filp = (i - self.zeros[i] + 1) +  self.ones[i+1]
            # i to one
            if minFip > filp:
                minFip = filp
        return min(minFip, self.ones[0])




# @lc code=end


s = Solution()
print(s.minFlipsMonoIncr("11011"))
print(s.minFlipsMonoIncr("10011111110010111011"))
s = Solution()
print(s.minFlipsMonoIncr("00011000"))
s = Solution()
print(s.minFlipsMonoIncr("00110"))
s = Solution()
s.minFlipsMonoIncr("010110")
