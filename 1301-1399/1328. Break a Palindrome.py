class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        mid = int(len(palindrome) / 2)
        f = False
        for i in range(0, mid):
            if palindrome[i] != 'a':
                f = True
                palindrome = palindrome[0:i] + 'a' + palindrome[i + 1:]
                break
        if not f:
            return palindrome[0:len(palindrome) - 1] + 'b'

        return palindrome


if __name__ == '__main__':
    s = Solution()
    print(s.breakPalindrome("aba"))
    print(s.breakPalindrome("abccba"))
    print(s.breakPalindrome("aaaaaa"))
