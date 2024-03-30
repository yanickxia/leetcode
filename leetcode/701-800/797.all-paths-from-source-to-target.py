#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # bfs
        Q = []
        ans = []
        last = len(graph) - 1
        for i in range(0, len(graph[0])):
            Q.append([0, graph[0][i]])
        while len(Q) != 0:
            current = Q.pop()
            if current[-1] == last:
                ans.append(current)
            for i in range(0, len(graph[current[-1]])):
                new = current.copy()
                new.append(graph[current[-1]][i])
                Q.append(new)
        return ans

    # @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[1, 2], [3], [3], []]))
    print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
