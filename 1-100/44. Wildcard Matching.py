class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0

        if s == p:
            return True

        if len(s) > 0 and len(p) > 0 and p[0].isalpha() and p[0] != s[0]:
            return False
        if len(s) > 0 and len(p) > 0 and p[-1].isalpha() and p[-1] != s[-1]:
            return False

        def all_index(sub: str, c: str):
            rs = []
            for x in range(len(sub)):
                if sub[x] == c:
                    rs.append(x)
            return rs

        while j < len(p):
            curr = p[j]
            if curr == '?':
                if i >= len(s):
                    return False
                i += 1
                j += 1
            elif curr == '*':
                should_letters = 0
                while j < len(p) and (p[j] == '*' or p[j] == '?'):
                    if p[j] == "?":
                        should_letters += 1
                    j += 1

                if j == len(p) and (len(s) - i) >= should_letters:
                    return True
                elif j == len(p):
                    return False

                # 子问题, 
                sub_s = s[i + should_letters:]
                maybe = all_index(sub_s, p[j])
                for maybe_index in maybe:
                    if self.isMatch(sub_s[maybe_index:], p[j:]):
                        return True
                return False

            else:
                if i >= len(s) or curr != s[i]:
                    return False
                i += 1
                j += 1
        if i < len(s):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch(
        "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
        "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
    print(s.isMatch("", "a"))
    print(s.isMatch("", ""))
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
