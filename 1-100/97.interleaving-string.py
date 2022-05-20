#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def __init__(self):
        self.notway = {}
        self.counter = 0

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 + len2 != len3):
            return False
        dp = [[False] * (len2 + 1) for i in range(len1 + 1)]
        dp[0][0] = True
        for i in range(1, len1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for i in range(1, len2 + 1):
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                            dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]

# @lc code=end



# class Solution:
#     def __init__(self):
#         self.notway = {}
#         self.counter = 0
#
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         self.counter += 1
#
#         if s1 + "," + s2 in self.notway or s2 + "," + s1 in self.notway:
#             return False
#
#         # print("compare\ns1:" + s1 + "\ns2:" + s2 + "\ns3:" + s3 + "\ncounter=" + str(self.counter))
#         if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
#             return True
#
#         if len(s1) + len(s2) != len(s3):
#             return False
#
#         if len(s1) == 0:
#             return s2 == s3
#         if len(s2) == 0:
#             return s1 == s3
#
#         if s1[0] == s3[0]:
#             l1 = 1
#             while s1[0:l1] == s3[0:l1]:
#                 l2 = 1
#                 while s2[0:l2] == s3[l1:l1 + l2]:
#                     if self.isInterleave(s1[l1:], s2[l2:], s3[l1 + l2:]):
#                         return True
#                     l2 += 1
#                 l1 += 1
#
#         if s2[0] == s3[0]:
#             l1 = 1
#             while s2[0:l1] == s3[0:l1]:
#                 l2 = 1
#                 while s1[0:l2] == s3[l1:l1 + l2]:
#                     if self.isInterleave(s1[l2:], s2[l1:], s3[l1 + l2:]):
#                         return True
#                     l2 += 1
#                 l1 += 1
#
#         self.notway[s1 + "," + s2] = 1
#         return False

if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave(
        "abababababababababababababababababababababababababababababababababababababababababababababababababbb",
        "babababababababababababababababababababababababababababababababababababababababababababababababaaaba",
        "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb"))

    print(s.isInterleave("cacbbbaaabbacbbbbabbcaccccabaaacacbcaacababbaabbaccacbaabac",
                         "cbcccabbbbaaacbaccbabaabbccbbbabacbaacccbbcaabaabbbcbcbab",
                         "ccbcccacbabbbbbbaaaaabbaaccbabbbbacbcbcbaacccbacabbaccbaaabcacbbcabaabacbbcaacaccbbacaabababaabbbaccbbcacbbacabbaacb"))
    print(s.isInterleave("aa", "ab", "abaa"))
    print(s.isInterleave("aabc", "abad", "aabacbad"))
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
