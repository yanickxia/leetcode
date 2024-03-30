class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # 状态数组，表示从s的i到p的j是否可以匹配
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = True
        # 当s为空时必须有*才可能满足匹配，并且他的真值一定和去掉*及其前面的符号相同
        for j in range(1, n + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 当 p上一个字符为'？'或者p上一个字符等于s上一个字符，则当前真值与上一位相同
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # p上一个字符为'*'时，则*可表示p往后走一位或者s往后走一位
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        # 返回s[0->len(s)] 与 p[0->len(p)]的真值
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()

    print(s.isMatch(
        "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
        "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
    print(s.isMatch("abefcdgiescdfimde", "ab*cd?i*de") == True)
    print(s.isMatch("mississippi", "m??*ss*?i*pi") == False)
    print(s.isMatch("aaaa", "***a") == True)
    print(s.isMatch("aa", "a*") == True)
    print(s.isMatch("aa", "*") == True)
    print(s.isMatch("", "a") == False)
    print(s.isMatch("", "") == True)
    print(s.isMatch(
        "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
        "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
    print(s.isMatch(
        "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
        "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"))
    print(s.isMatch("b", "?*?") == False)
    print(s.isMatch("acdcb", "a*c?b") == False)
    print(s.isMatch("cb", "?a") == False)
    print(s.isMatch("adceb", "*a*b") == True)
    print(s.isMatch("abcdabed", "*a?ed") == True)
    print(s.isMatch("aa", "*") == True)
    print(s.isMatch("aa", "aa") == True)
    print(s.isMatch("aa", "a") == False)
    print(s.isMatch("a", "aa") == False)
