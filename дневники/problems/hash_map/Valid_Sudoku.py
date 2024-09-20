'''
ПРАВИЛЬНОЕ СУДОКУ

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks = {}
        for i in range(len(board)):
            str_list = {}
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in str_list:
                    return False
                str_list[board[i][j]] = 1
                b = i // 3 * 3 + j // 3
                if b not in blocks:
                    blocks[b] = []
                if board[i][j] not in blocks[b]:
                    blocks[b].append(board[i][j])
                else:
                    return False

            
        for i in range(len(board)):
            colomn_list = {}
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colomn_list:
                    return False
                colomn_list[board[j][i]] = 1

                 
        return True
   

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                if val in rows[i] or val in cols[j] or val in blocks[i // 3 * 3 + j // 3]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                blocks[i // 3 * 3 + j // 3].add(val)

        return True