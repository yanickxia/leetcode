# -*- coding:utf-8 -*-

import math


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
        # self.file = open('res.txt','w')

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(0, 9):
            for j in range(0, 9):
                regin = self.i_j_to_regin(i, j)
                if self.regin_cache.get(regin) is None:
                    self.regin_cache[regin] = []
                self.regin_cache[regin].append((i, j))

                if board[i][j] == '.':
                    self.need_fill.append((i, j))

        self.solve_sudoku(board, None, self.need_fill)
        # self.print_sudoku(board)
        # print(board)

    def solve_sudoku(self, board, pre, need_fill_pos):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if self.is_find:
            return

        # self.print_sudoku(board)

        if len(need_fill_pos) == 0:
            self.is_find = True
            return

        curren_pos = need_fill_pos[0]
        i, j = curren_pos[0], curren_pos[1]
        numbs = self.find_avail_numbers(board, i, j)
        # print(numbs)
        if numbs is []:
            board[pre[0]][pre[1]] = '.'
            return

        for num in numbs:
            board[i][j] = num
            self.solve_sudoku(board, curren_pos, need_fill_pos[1:])
            if self.is_find:
                return

        if self.is_find:
            return

        if board[i][j] == '.':
            board[pre[0]][pre[1]] = '.'

        return

    def find_avail_numbers(self, board, i, j):
        # row
        one_board_rem = set([int(x) for x in board[i] if x != '.'])

        # col
        for line in board:
            x = line[j]
            if x != '.':
                one_board_rem.add(int(x))

        # regin
        points = self.regin_cache.get(self.i_j_to_regin(i, j))
        for p in points:
            x = board[p[0]][p[1]]
            if x != '.':
                one_board_rem.add(int(x))

        return [str(x) for x in self.numbers.difference(one_board_rem)]

    def i_j_to_regin(self, i, j):
        return (i / 3) * 3 + (j / 3) + 1

    def print_sudoku(self, array):
        for line in array:
            for x in line:
                print x + ' ',
            print('\n')
        print('\n\n')


s = Solution()

assert s.i_j_to_regin(0, 0) == 1
assert s.i_j_to_regin(1, 1) == 1
assert s.i_j_to_regin(5, 5) == 5
assert s.i_j_to_regin(8, 8) == 9
assert s.i_j_to_regin(7, 5) == 8

# input_r = [["5", "3", ".", "6", ".", ".", ".", "9", "8"],
#            [".", "7", ".", "1", "9", "5", ".", ".", "."],
#            [".", ".", ".", ".", ".", ".", ".", "6", "."],
#            ["8", ".", ".", "4", ".", ".", "7", ".", "."],
#            [".", "6", ".", "8", ".", "3", ".", "2", "."],
#            [".", ".", "3", ".", ".", "1", ".", ".", "6"],
#            [".", "6", ".", ".", ".", ".", ".", ".", "."],
#            [".", ".", ".", "4", "1", "9", ".", "8", "."],
#            ["2", "8", ".", ".", ".", "5", ".", "7", "9"]]

input_r = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
           [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
           [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
           [".", ".", ".", "2", "7", "5", "9", ".", "."]]

# input_r = [["5", "1", "9", "7", "4", "8", "6", "3", "2"], ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
#            ["4", "2", "6", "1", "3", "9", "8", "7", "5"], [".", ".", "7", ".", ".", ".", "2", "4", "."],
#            [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
#            [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#            [".", ".", ".", "2", "7", "5", "9", ".", "."]]
#
# s.print_sudoku([["5", "1", "9", "7", "4", "8", "6", "3", "2"], ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
#                 ["4", "2", "6", "1", "3", "9", "8", "7", "5"], ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
#                 ["2", "6", "4", "3", "1", "7", "5", "9", "8"], ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
#                 ["9", "7", "5", "8", "6", "3", "1", "2", "4"], ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
#                 ["6", "4", "1", "2", "7", "5", "9", "8", "3"]]
#                )


s.solveSudoku(input_r)
