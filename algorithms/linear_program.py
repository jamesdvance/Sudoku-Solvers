from pulp import (LpProblem, 
    LpVariable, 
    LpInteger, 
    LpMinimize, 
    lpSum,
    LpStatus,
    value)
import numpy as np


def linear_program(board):

    seq = list(range(1,10))
    vals = seq.copy()
    rows = seq.copy()
    cols = seq.copy()
        

    boxes = [] 
    for i in range(3):
        for j in range(3):
            boxes += [[(rows[3*i+k], cols[3*j+l]) for k in range(3) for l in range(3)]]


    prob = LpProblem("Sudoku", LpMinimize)
    choices = LpVariable.dicts("Choice", (vals,rows,cols),0,1,LpInteger)
    prob += 0 # objective function. This is a list I guess 
    for r in rows:
        for c in cols:
            prob += lpSum([choices[v][r][c] for v in vals]) == 1, ""

    for v in vals:
        for r in rows:
            prob += lpSum([choices[v][r][c] for c in cols]) == 1, ""
        for c in cols:
            prob += lpSum([choices[v][r][c] for r in rows]) == 1, ""
        for b in boxes:
            prob += lpSum([choices[v][r][c] for (r,c) in b]) == 1,""


    for r in rows:
        for c in cols:
            if board[r-1,c-1] != 0:
                print(f"Setting row {r-1} col {c-1} to {board[r-1,c-1]}")
                
                prob += choices[board[r-1,c-1]][r][c] == 1,""

    prob.writeLP("Sudoku.lp")
    prob.solve()

    status = LpStatus[prob.status]
    if status != "Optimal":
        raise ValueError(f"Solution status '{status}' instead of 'Optimal'")

    for v in vals:
        for r in rows:
            for c in cols:
                if value(choices[v][r][c]) == 1.0:
                    board[r-1,c-1] = v

    return board