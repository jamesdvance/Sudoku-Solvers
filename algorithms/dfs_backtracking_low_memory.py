
import numpy as np 
"""
For more about this solution, browse solutions here
https://leetcode.com/problems/sudoku-solver/
"""
from typing import List
from collections import defaultdict 
from utils import timethis # path in first 

def isValid(board: np.ndarray, 
    row:int, 
    col:int, 
    candidate:str)->bool:
    if any([board[row][j] == candidate for j in range(9) if j != col]): 
        return False # check col
    if any([board[j][col] == candidate for j in range(9) if j != row]): 
        return False # check row
    br,bc = 3*(row//3), 3*(col//3)
    if any([board[i][j] == candidate for i in range(br, br+3) for j in range(bc,bc+3)]): 
        return False # square
    return True

@timethis
def dfs_backtracking_low_memory(board:np.ndarray) -> np.ndarray:
    """
    DFS (Backtracking)
    """
    def backtrack(row, col):
        nonlocal board
        # get next position that is 0
        while board[row][col] != 0:
            col += 1
            if col == 9: 
                col, row = 0, row+1
            if row ==9: 
                return True

        # backtrack
        for k in range(1,10):
            if isValid(board, row, col, k):
                board[row][col] = k 
                if backtrack(row,col): # We've overwritten 0 for current row, so no need to move forward. backtrack will move us forward on next call
                    return True 

        board[row][col] = 0
        return False

    backtrack(0,0)
    return board



