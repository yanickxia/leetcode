class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0

        def all_index(sub: str, c: str):
            rs = []
            begin = 0
            while begin < len(sub):
                found = sub.find(c, begin)
                if found >= 0:
                    rs.append(found)
                    begin +=  found +1
                else:
                    break
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

                # 子问题, 最好处理下连续的字符
                c = ''
                while j < len(p) and p[j] != '*' and p[j] != '?':
                    c += p[j]
                    j += 1

                sub_s = s[i + should_letters:]
                maybe = all_index(sub_s, c)
                for maybe_index in maybe:
                    if self.isMatch(sub_s[maybe_index:], p[j-1:]):
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
    print(s.isMatch("adceb", "*a*b") == True)
    print(s.isMatch(
        "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
        "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
    print(s.isMatch(
        "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
        "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"))
    print(s.isMatch("b", "?*?"))
    print(s.isMatch("acdcb", "a*c?b") == False)
    print(s.isMatch("cb", "?a") == False)
    print(s.isMatch("abcdabed", "*a?ed") == True)
    print(s.isMatch("aa", "*") == True)
    print(s.isMatch("aa", "aa") == True)
    print(s.isMatch("aa", "a") == False)
    print(s.isMatch("a", "aa") == False)
