class Solution:
    def longestPalindrome(self, s: str) -> int:
        words = {}
        for i in range(0, len(s)):
            if s[i] not in words:
                words[s[i]] = 1
            else:
                words[s[i]] += 1
        longest = 0
        for k, v in words.items():
            if v > 1:
                longest += (int(v / 2) * 2)
        if longest < len(s):
            longest += 1
        return longest


s = Solution()
print(s.longestPalindrome("a"))
print(s.longestPalindrome("abccccdd"))
