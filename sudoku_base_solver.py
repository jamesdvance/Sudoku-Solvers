import abc 
from dataclasses import dataclass 
from typing import List, FrozenSet
import gym
from gym.spaces import Box

@dataclass 
class Board():

    board: List[List[str]]
    open_spaces: int
    length: int = len(board)
    width: int = len(board[0])
    digits: FrozenSet[str] = [str(i) for i in range(1, 10)] 

    @property
    def set_board(self, board):
        self.board = board

    def _get_open_spaces(self):
        count = 0 
        for row in range(self.length):
            for col in range(self.width):
                if self.board[row][col] not in self.digits: 
                    count+=1

        return count

    @property
    def is_solved(self):
        return self._get_open_spaces() == 0

    @property
    def is_valid_board(self):
        return (self.width == self.length 
            and self._get_open_spaces == self.open_spaces)

    @property
    def is_valid_solution(self):
        if self.board


class SudokuSolver(abc.ABC):

    def __init__(self, board:Board):
        # TODO - add board validation
        # assign
        self.board = board.board

    @abc.abstractmethod
    def solve(self)->Board:
        pass


