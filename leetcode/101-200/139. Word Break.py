class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = sorted(wordDict)
        f = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for k in range(i):
                if f[k] and s[k:i] in wordDict:
                    f[i] = True

        return f[-1]


s = Solution()

print(s.wordBreak('abbs', ["a", "bb", "b", "s"]))
print(s.wordBreak('leetcode', ["leet", "code"]))

print(s.wordBreak("cars",
                  ["car", "ca", "rs"]))
