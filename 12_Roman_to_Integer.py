__author__ = 'yann'


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and Solution.isLeft(s[i], s[i + 1]):
                result -= Solution.getIntFromStr(s[i])
                result += Solution.getIntFromStr(s[i + 1])
                i += 2
            else:
                result += Solution.getIntFromStr(s[i])
                i += 1

        return result

    @staticmethod
    def getIntFromStr(s):
        if s == 'I':
            return 1
        elif s == 'X':
            return 10
        elif s == 'C':
            return 100
        elif s == 'M':
            return 1000
        elif s == 'V':
            return 5
        elif s == 'L':
            return 50
        elif s == 'D':
            return 500

    @staticmethod
    def isLeft(s1, s2):
        if s1 in ['I', 'X', 'C'] and Solution.getIntFromStr(s1) < Solution.getIntFromStr(s2):
            return True
        return False

s = Solution()

assert s.romanToInt('MCMLXXX') == 1980
assert s.romanToInt('III') == 3
assert s.romanToInt('IV') == 4
assert s.romanToInt('VI') == 6
assert s.romanToInt('XIX') == 19
assert s.romanToInt('XX') == 20
assert s.romanToInt('XLV') == 45

