# -*- coding:utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match_list = []
        for s_item in s:
            if s_item in ['(', '{', '[']:
                match_list.append(s_item)
            else:
                if len(match_list) == 0:
                    return False

                last_match = match_list[-1]
                if (s_item == ')' and last_match == '(') or  \
                    (s_item == '}' and last_match == '{') or  \
                    (s_item == ']' and last_match == '['):

                    del match_list[-1]
                else:
                    return False

        return len(match_list) == 0


s = Solution()
print s.isValid("()[]{}")