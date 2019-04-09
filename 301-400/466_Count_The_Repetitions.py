# -*- coding:utf-8 -*-


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if s1 == s2:
            return int(n1 / n2)

        # nothing found
        if not set(list(s1)).issuperset(set(list(s2))):
            return 0

        for i in range(1, n1):
            for j in range(1, n2):
                if Solution.perfect_match(s1 * i, s2 * j):
                    return (n1 / i) / (n2 / j)
        return 1

    @staticmethod
    def contain(s1, s2):
        i = 0
        while i < len(s2):
            if s2[i] in s1:
                s1 = s1[s1.index(s2[i]) + 1:]
                i += 1
        if i == len(s2) - 1:
            return True, None
        return False, s2[:len(s2) - i]


    @staticmethod
    def perfect_match(s1, s2):
        i, j = 0, 0
        while i < len(s1):
            if s1[i] == s2[j]:
                j += 1
            i += 1

        return i == len(s1) and j == len(s2)


if __name__ == '__main__':
    s = Solution()
    print s.getMaxRepetitions("abc", 4, "ab", 2)
    # print s.getMaxRepetitions("baba", 11, "baab", 1)
    print s.getMaxRepetitions("acb", 1, "acb", 1)
