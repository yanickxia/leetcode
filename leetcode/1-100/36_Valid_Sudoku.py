# -*- coding:utf-8 -*-

class Solution(object):

    def __init__(self):
        self.row_cache = {}
        self.row_v_cache = {}
        self.col_cache = {}
        self.col_v_cache = {}
        self.regin_cache = {}
        self.is_find = False
        self.numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.need_fill = []

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9):
            for j in range(0, 9):
                regin = self.i_j_to_regin(i, j)
                if self.regin_cache.get(regin) is None:
                    self.regin_cache[regin] = []
                self.regin_cache[regin].append((i, j))

        # check row
        for i in range(0, 9):
            if not self.is_vail_list(board[i]):
                return False
        # check col
        for i in range(0, 9):
            cols = []
            for j in range(0, 9):
                cols.append(board[j][i])
            if not self.is_vail_list(cols):
                return False
        # check regin
        for i in range(1, 10):
            regs = self.regin_cache.get(i)
            regs_n = []
            for pos in regs:
                regs_n.append(board[pos[0]][pos[1]])
            if not self.is_vail_list(regs_n):
                return False
        return True

    def i_j_to_regin(self, i, j):
        return (i / 3) * 3 + (j / 3) + 1

    def is_vail_list(self, lst):
        lst = [x for x in lst if x != '.']
        return len(set(lst)) == len(lst)


s = Solution()
s.isValidSudoku([[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
                ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
                ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
                ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
               )
