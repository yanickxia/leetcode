# -*- coding:utf-8 -*-

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        rs = {}
        for item in strs:
            it_key = ''.join(sorted(list(item)))
            if rs.get(it_key) is None:
                rs[it_key] = [item]
            else:
                rs[it_key].append(item)
        n_rs = []
        for (k, v) in rs.iteritems():
            n_rs.append(v)

        return n_rs


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
