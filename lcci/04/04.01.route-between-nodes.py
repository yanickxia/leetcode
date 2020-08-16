import collections
from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:

        queue = collections.deque()
        visted = set()

        for i in range(len(graph)):
            if graph[i][0] == start and str(graph[i]) not in visted:
                queue.append(graph[i])
                visted.add(str(graph[i]))

        if len(queue) == 0:
            return False

        while queue:
            cur = queue.pop()
            if cur[1] == target:
                return True

            for i in range(len(graph)):
                if graph[i][0] == cur[1] and str(graph[i]) not in visted:
                    queue.append(graph[i])
                    visted.add(str(graph[i]))

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.findWhetherExistsPath(3, [[0, 1], [0, 2], [1, 2], [1, 2]], 0, 2))
    print(s.findWhetherExistsPath(n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4))
    print(s.findWhetherExistsPath(25,[[0, 1], [0, 3], [0, 10], [0, 18], [1, 2], [1, 7], [1, 11], [1, 12], [2, 4], [2, 5], [2, 13], [2, 16], [3, 6], [3, 8], [4, 9], [5, 17], [7, 20], [7, 22], [8, 10], [10, 19], [11, 15], [13, 14], [14, 21], [15, 23], [19, 24], [20, 22]],0,12))