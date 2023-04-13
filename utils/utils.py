import numpy as np 
import time
from functools import wraps
__all__=['get_solutions', 'check_solution', 'timethis']

resolved = 0
unfinished = 1
error = 2

def countItem(vector, item):
	count = 0
	for item2 in vector:
		if item2 == item: count += 1
	return count

# Check a solution is correct by checking the 3 contraints on all digits
#	- digit is unique in row
#	- digit is unique in column
#	- digit is unique in square
#  @return
#	- resolved if the grid is resolved
#	- unfinished if the grid is not yet finished
#	- error if one of the contraints is not respected
def check_solution(grid):
	N = len(grid)

	for i in range(N):
		for j in range(N):
			# If a case is not filled, the sudoku is not finished
			if grid[i][j] == 0:
				return "Unfinished"

			n = N//3
			iOffset = i//n*n
			jOffset = j//n*n
			square = grid[ iOffset:iOffset + n , jOffset:jOffset + n].flatten()
			# Check uniqueness
			uniqueInRow    = countItem(grid[i], grid[i, j])  == 1
			uniqueInCol    = countItem(grid[:,j:j+1].flatten(), grid[i, j]) == 1
			uniqueInSquare = countItem(square, grid[i, j]) == 1

			if not (uniqueInRow and uniqueInCol and uniqueInSquare):
				return "Error"

	return "Solved"


# Count the number of time the item appears in a vector



# Recursivly find all solutions (backtracking)
# @param stopAt make the backtracking stop when it found x solutions
# @param i, j force to start the backtracking from the case (i, j)
# @param omit prevent looking into a possibility
def get_solutions(grid, stopAt=1, i=-1, j=-1, omit=-1):
	N = len(grid)
	check = check_solution(grid)
	# Check if grid is resolve or if there is an error
	if check == resolved:
		return np.array([grid], dtype=int)
	if check == error:
		return np.empty(shape=(0,N,N), dtype=int)

	# If i and j are not setted, get the first empty spot and start backtracking from it
	if i == -1:
		for i in range(N):
			for j in range(N):
				# If not empty spot continue
				if grid[i, j] == 0: break
			if grid[i, j] == 0: break

	# Randomize possible values
	values = np.arange(1, N+1)
	np.random.shuffle(values)
	# Try all possiblities from those values until we reach the max nb of solutions asked by stopAt
	solutions = np.empty(shape=(0,N,N), dtype=int)
	for value in values:
		if omit == value: continue
		cGrid = np.copy(grid)
		cGrid[i, j] = value
		subSolutions = get_solutions(cGrid, stopAt=stopAt-len(solutions))
		solutions = np.concatenate((solutions, subSolutions))
		if len(solutions) >= stopAt:
			return solutions
	return solutions

def timethis(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		r =func(*args, **kwargs)
		end = time.perf_counter()
		print(f"{func.__module__}: {(end-start)*1000} ms ")
		return r 
	return wrapper

