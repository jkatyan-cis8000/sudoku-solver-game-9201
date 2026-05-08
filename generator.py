import random
from board import Board, GRID_SIZE, SUBGRID_SIZE, EMPTY
from validator import validate_move, is_complete


def _solve_backtrack(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board.get_cell(row, col) == EMPTY:
                for value in range(1, 10):
                    if validate_move(board, row, col, value):
                        board.set_cell(row, col, value)
                        if _solve_backtrack(board):
                            return True
                        board.set_cell(row, col, EMPTY)
                return False
    return True


def solve_sudoku(board):
    solution = board.copy()
    if _solve_backtrack(solution):
        return solution
    return None


def _generate_full_board():
    board = Board()
    _solve_backtrack(board)
    return board


def _remove_numbers(full_board, holes):
    board = full_board.copy()
    cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)]
    random.shuffle(cells)
    
    for row, col in cells[:holes]:
        board.set_cell(row, col, EMPTY)
    
    return board


def generate_puzzle(difficulty='medium'):
    difficulty_holes = {
        'easy': 30,
        'medium': 40,
        'hard': 50,
        'expert': 60
    }
    
    holes = difficulty_holes.get(difficulty.lower(), 40)
    
    full_board = _generate_full_board()
    puzzle = _remove_numbers(full_board, holes)
    
    return puzzle, full_board
