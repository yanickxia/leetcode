class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(board[i] - j) == abs(k - i):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:
                res.append(valuelist)
                return
            else:
                for i in range(n):
                    if check(depth, i):
                        board[depth] = i
                        s = '.' * n
                        dfs(depth + 1, valuelist + [s[:i] + 'Q' + s[i + 1:]])

        res = []
        board = [-1 for i in range(n)]
        dfs(0, [])
        return res
