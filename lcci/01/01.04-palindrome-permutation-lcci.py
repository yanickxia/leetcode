class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return False
        chars = {}
        for i in range(len(s)):
            c = s[i]
            if c not in chars:
                chars[c] = 0

            if chars[c] == 1:
                chars[c] =0
            else:
                chars[c] =1
        odd_count = 0
        for c in chars:
            if chars[c] == 1:
                odd_count+=1


        return len(s) % 2 == odd_count

if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("tactcoa"))
    print(s.canPermutePalindrome("ab"))