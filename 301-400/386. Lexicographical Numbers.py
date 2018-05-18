# -*- coding:utf-8 -*-

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rs = {}
        root_rs = rs
        i = 0
        level_cache = {}
        current_level = 1
        while i <= n:
            i += 1
            lv = len(str(i))
            if lv > current_level:
                current_level += 1
                rs = level_cache[lv - 1]

            if rs.get(int(i / 10)) is None:
                rs[i] = {}
                if level_cache.get(lv) is None:
                    level_cache[lv] = {}
                level_cache[lv][i] = rs.get(i)
            else:
                rs.get(int(i / 10))[i] = {}
                if level_cache.get(lv) is None:
                    level_cache[lv] = {}
                level_cache[lv][i] = rs.get(int(i / 10))[i]
            ts = []
            self.travel_map_to_list(root_rs, ts)
        return ts

    def travel_map_to_list(self, rs, lst):
        for k in rs.keys():
            lst.append(k)
            if rs.get(k) is not {}:
                self.travel_map_to_list(rs.get(k), lst)


s = Solution()
print(s.lexicalOrder(5000))
