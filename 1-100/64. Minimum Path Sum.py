# -*- coding:utf-8 -*-

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(grid)):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in xrange(1, len(grid[0])):
            grid[0][j] = grid[0][j - 1] + grid[0][j]

        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[i])):
                grid[i][j] = min(grid[i - 1][j] + grid[i][j], grid[i][j - 1] + grid[i][j])

        return grid[-1][-1]


s = Solution()
print(s.minPathSum([[1, 3, 1],
                    [1, 5, 1],
                    [4, 2, 1]]))
