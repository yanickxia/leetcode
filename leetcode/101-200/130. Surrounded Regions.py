import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    queue = collections.deque()
                    queue.append((i, j))
                    visited = {(i, j)}
                    flag = self.__bfs(board, queue, visited, i, j)
                    if flag:
                        for x in visited:
                            board[x[0]][x[1]] = 'X'

    def __bfs(self, board: List[List[str]], queue, visited, i, j) -> bool:
        m = len(board)
        n = len(board[0])

        while queue:
            i, j = queue.pop()

            if i > 0 and board[i - 1][j] == 'O' and (i - 1, j) not in visited:
                queue.append((i - 1, j))
                visited.add((i - 1, j))
            if i < m - 1 and board[i + 1][j] == 'O' and (i + 1, j) not in visited:
                queue.append((i + 1, j))
                visited.add((i + 1, j))
            if j > 0 and board[i][j - 1] == 'O' and (i, j - 1) not in visited:
                queue.append((i, j - 1))
                visited.add((i, j - 1))
            if j < n - 1 and board[i][j + 1] == 'O' and (i, j + 1) not in visited:
                queue.append((i, j + 1))
                visited.add((i, j + 1))

        for x in visited:
            if x[0] == 0 or x[0] == m - 1 or x[1] == 0 or x[1] == n - 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
