from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        ans = []
        for i in range(n):
            max_width = 1
            for j in range(len(grid)):
                max_width = max(max_width, len(str(grid[j][i])))
            ans.append(max_width)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findColumnWidth([[1],[22],[333]]))