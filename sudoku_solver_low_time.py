from sudoku_base_solver import SudokuSolver

"""
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Input: board = [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
"""
from typing import List
from collections import defaultdict 
class Solution:
    def solve(self) -> None:
        """
        Do not return anything, modify board in-place instead.

        This solution optimizes memory over speed
        """
        board = self.board
        rows, cols = defaultdict(), defaultdict()
        square = defaultdict()
        def backtrack(row, col):
            nonlocal board
            # get next position that is "."
            while board[row][col] != ".":
                col += 1
                if col == 9: 
                    col, row = 0, row+1
                if row ==9: 
                    return True

            # backtrack
            for k in range(1,10):
                if self.isValid(board, row, col, str(k)):
                    board[row][col] = str(k) # convert to string for comparison to strings in board
                    if backtrack(row,col): # We've overwritten "." for current row, so no need to move forward. backtrack will move us forward on next call
                        return True 

            board[row][col] = "."
            return False

        return backtrack(0,0)

    def isValid(self, 
        board: List[List[str]], 
        row:int, 
        col:int, 
        candidate:str)->bool:
        if any([board[row][j] == candidate for j in range(9) if j != col]): return False # check col
        if any([board[j][col] == candidate for j in range(9) if j != row]): return False # check row
        br,bc = 3*(row//3), 3*(col//3)
        if any([board[i][j] == candidate for i in range(br, br+3) for j in range(bc,bc+3)]): return False # square
        return True

