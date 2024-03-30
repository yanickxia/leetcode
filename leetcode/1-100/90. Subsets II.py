# -*- coding:utf-8 -*-

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def dfs(depth, start, valuelist):
            if valuelist not in res: res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth + 1, i + 1, valuelist + [S[i]])

        S.sort()
        res = []
        dfs(0, 0, [])
        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
