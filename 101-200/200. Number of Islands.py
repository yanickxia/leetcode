# -*- coding:utf-8 -*-

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.clear_a_land(grid, (i, j))
        return count

    def clear_a_land(self, grid, pos):
        i, j = pos[0], pos[1]
        need_clear_pos = []
        if i > 0 and grid[i - 1][j] == "1":
            need_clear_pos.append((i - 1, j))
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            need_clear_pos.append((i + 1, j))
        if j > 0 and grid[i][j - 1] == "1":
            need_clear_pos.append((i, j - 1))
        if j < len(grid[i]) - 1 and grid[i][j + 1] == "1":
            need_clear_pos.append((i, j + 1))
        grid[i][j] = "0"
        for x in need_clear_pos:
            self.clear_a_land(grid, x)


s = Solution()
print(s.numIslands([["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]]))

print(s.numIslands([["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"]]))
