from board import Board
from generator import generate_puzzle
from validator import validate_move, is_valid_solution, check_conflicts, is_complete


class SudokuGame:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.solution = None
        self.mistakes = 0
        self._initialize_game()
    
    def _initialize_game(self):
        puzzle, self.solution = generate_puzzle(self.difficulty)
        self.board = puzzle
        self.initial_board = puzzle.copy()
    
    def display(self):
        print(self.board.to_string())
        print(f"\nMistakes: {self.mistakes}")
    
    def make_move(self, row, col, value):
        if not (0 <= row < 9 and 0 <= col < 9):
            return False, "Invalid position"
        
        if not (1 <= value <= 9):
            return False, "Invalid value"
        
        if self.initial_board.get_cell(row, col) != 0:
            return False, "Cannot modify pre-filled cell"
        
        if not validate_move(self.board, row, col, value):
            self.mistakes += 1
            return False, "Invalid move"
        
        self.board.set_cell(row, col, value)
        return True, None
    
    def check_mistakes(self):
        return self.mistakes
    
    def is_solved(self):
        if not is_complete(self.board):
            return False
        return is_valid_solution(self.board)
    
    def get_hint(self, row, col):
        if not (0 <= row < 9 and 0 <= col < 9):
            return None
        
        if self.board.get_cell(row, col) != 0:
            return self.board.get_cell(row, col)
        
        return self.solution.get_cell(row, col)
    
    def solve(self):
        self.board = self.solution.copy()
