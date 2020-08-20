import collections
import itertools
from typing import List


class Solution:
    def uniquePathsIII(self, G: List[List[int]]) -> int:
        M, N, t, z = len(G), len(G[0]), [0], 0
        for i,j in itertools.product(range(M),range(N)):
            if G[i][j] == 0: z += 1
            if G[i][j] == 1: a,b = i,j
            if G[i][j] == 2: e,f = i,j
        G[a][b] = 0
        def dfs(i,j,c):
            if (i,j) == (e,f): t[0] += (c == z+1)
            if G[i][j]: return
            G[i][j] = -1
            for x,y in (i-1,j),(i,j+1),(i+1,j),(i,j-1): 0<=x<M and 0<=y<N and dfs(x,y,c+1)
            G[i][j] = 0
        dfs(a,b,0)
        return t[0]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
    print(s.uniquePathsIII([
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]
    ]))
