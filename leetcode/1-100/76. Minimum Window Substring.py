# -*- coding:utf-8 -*-

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map = {}
        for i in xrange(len(t)):
            if t_map.get(t[i]) is None:
                t_map[t[i]] = 1
            else:
                t_map[t[i]] = t_map[t[i]] + 1

        current_range = (0, len(s))
        i, j = 0, -1
        while i < len(s):

            if Solution.is_matched(t_map):
                if j - i < (current_range[1] - current_range[0]):
                    current_range = (i, j)

            while j < len(s) - 1:
                if Solution.is_matched(t_map):
                    if j - i < (current_range[1] - current_range[0]):
                        current_range = (i, j)
                    break

                j += 1

                if t_map.get(s[j]) is not None:
                    t_map[s[j]] = t_map.get(s[j]) - 1

            if Solution.is_matched(t_map):
                if j - i < (current_range[1] - current_range[0]):
                    current_range = (i, j)

            if t_map.get(s[i]) is not None:
                t_map[s[i]] = t_map.get(s[i]) + 1
            i += 1

        if current_range[1] == len(s):
            return ""

        return s[current_range[0]:current_range[1] + 1]

    @staticmethod
    def is_matched(mp):
        for key in mp.keys():
            if mp[key] > 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.minWindow("ADOBECODEBANC", "ABC")
    print s.minWindow("a", "aa")
    print s.minWindow("a", "a")