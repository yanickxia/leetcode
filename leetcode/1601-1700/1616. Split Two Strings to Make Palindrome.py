class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) == 1:
            return True

        return self.check(a, b) or self.check(b, a)

    def check(self, a: str, b: str) -> bool:
        i, j = 0, len(a) - 1
        while a[i] == b[j]:
            i += 1
            j -= 1
        return a[i:j + 1] == a[i:j + 1][::-1] or b[i:j + 1] == b[i:j + 1][::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.checkPalindromeFormation("ulacfd", "jizalu"))
    print(s.checkPalindromeFormation("abda", "acmc") == False)

    print(s.checkPalindromeFormation("cddbcdbdc",
                                     "cdbccbddc"))

    print(s.checkPalindromeFormation("abdef", "fecab") == True)

    print(s.checkPalindromeFormation("ulacfddd", "ddjizalu") == False)
    print(s.checkPalindromeFormation("xbdef", "xecab") == False)
    print(s.checkPalindromeFormation("a", "b") == True)
