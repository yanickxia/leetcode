__author__ = 'yann'


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        s_l, t_l = [], []
        for i in range(0, len(s)):
            s_l.append(s[i])
            t_l.append(t[i])

        s_l = sorted(s_l)
        t_l = sorted(t_l)

        if len(s_l) == 0:
            return True

        for i in range(0, len(s_l)):
            if s_l[i] != t_l[i]:
                return False

        return True


s = Solution()
# print(s.isAnagram('', ''))
# print(s.isAnagram('anagram', 'nagaram'))
# print(s.isAnagram('rat', 'car'))
print(s.isAnagram('ccac', 'aacc'))

