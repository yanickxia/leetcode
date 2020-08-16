from collections import deque
from typing import List

# BFS
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        n = len(graph)
        adj = [[] for _ in range(n)]
        # 转为邻接表
        for i, j in graph:
            adj[i].append(j)
        # BFS
        queue = deque()
        queue.append(start)
        while queue:
            tmp = queue.popleft()
            if tmp == target:
                return True
            for i in adj[tmp]:
                queue.append(i)
        return False

# BFS
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        n = len(graph)
        adj = [[] for i in range(n)]
        for i, j in graph:
            adj[i].append(j)
        # 用一个标记数组来标记是否已经遍历过，如果已经遍历过，需要continue
        seen = [False for _ in range(n)]
        # DFS
        def dfs(start):
            seen[start] = True
            if start == target:
                return True
            for i in adj[start]:
                if not seen[i] and dfs(i):
                    return True
            return False

        return dfs(start)


if __name__ == '__main__':
    s = Solution()
    print(s.findWhetherExistsPath(3, [[0, 1], [0, 2], [1, 2], [1, 2]], 0, 2))
    print(s.findWhetherExistsPath(n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4))
    print(s.findWhetherExistsPath(25,[[0, 1], [0, 3], [0, 10], [0, 18], [1, 2], [1, 7], [1, 11], [1, 12], [2, 4], [2, 5], [2, 13], [2, 16], [3, 6], [3, 8], [4, 9], [5, 17], [7, 20], [7, 22], [8, 10], [10, 19], [11, 15], [13, 14], [14, 21], [15, 23], [19, 24], [20, 22]],0,12))
    print(s.findWhetherExistsPath(12,[[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10], [2, 4], [2, 5], [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7], [5, 10], [6, 8], [7, 11], [8, 10]],2,3))
    print(s.findWhetherExistsPath(20,[[0, 1], [0, 4], [0, 12], [1, 2], [1, 3], [1, 5], [2, 10], [3, 13], [5, 6], [5, 8], [5, 9], [5, 19], [6, 7], [8, 11], [8, 14], [10, 16], [11, 15], [12, 14], [14, 17], [14, 18]],8,11))