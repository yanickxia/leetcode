class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pos = [[0] * n] * m

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    pos[i][j] = 1
                else:
                    pos[i][j] = pos[i - 1][j] + pos[i][j - 1]

        return pos[-1][-1]


s = Solution()
print(s.uniquePaths(3, 7))
