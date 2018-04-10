# -*- coding:utf-8 -*-


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        start_of_word = word[0]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if start_of_word == board[i][j]:
                    if self.find_it_way(board, word[1:], [(i, j)]):
                        return True
        return False

    def find_it_way(self, board, word, pos):
        if len(word) == 0:
            return True
        pre = pos[-1]
        nexts = self.find_next_char_pos(board, word[0], pre, pos)
        if len(nexts) == 0:
            return False
        for next in nexts:
            np = list(pos)
            np.append(next)
            # 如果只用一个数组的回退思路有个没想出来

            if self.find_it_way(board, word[1:], np):
                return True

        return False

    def find_next_char_pos(self, board, c, a_pos, pos):
        height, weghit = len(board), len(board[0])
        rs = []
        if a_pos[1] > 0:
            x = (a_pos[0], a_pos[1] - 1)

            if x not in pos and board[x[0]][x[1]] == c:
                rs.append(x)
        if a_pos[1] < weghit - 1:
            x = (a_pos[0], a_pos[1] + 1)
            if x not in pos and board[x[0]][x[1]] == c:
                rs.append(x)
        if a_pos[0] > 0:
            x = (a_pos[0] - 1, a_pos[1])
            if x not in pos and board[x[0]][x[1]] == c:
                rs.append(x)
        if a_pos[0] < height - 1:
            x = (a_pos[0] + 1, a_pos[1])
            if x not in pos and board[x[0]][x[1]] == c:
                rs.append(x)
        return rs


s = Solution()
print(s.exist([["A", "B", "C", "E"],
               ["S", "F", "E", "S"],
               ["A", "D", "E", "E"]]
              , "ABCESEEEFS"))

# print(s.exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], "ABCCED"))
# print(s.exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], "SEE"))
# print(s.exist([
#     ['A', 'B', 'C', 'E'],
#     ['S', 'F', 'C', 'S'],
#     ['A', 'D', 'E', 'E']
# ], "ABCB"))
