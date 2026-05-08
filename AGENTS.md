# Sudoku Game Architecture

## Modules Overview

### 1. board.py - Board Management
**Responsibility**: Manages the 9x9 Sudoku grid, initialization, and basic operations.

**Interfaces**:
- `Board` class with:
  - `__init__():` Initialize empty 9x9 grid
  - `set_cell(row, col, value):` Set a cell value
  - `get_cell(row, col):` Get a cell value
  - `to_string():` Return string representation of board
  - `copy():` Create deep copy of board

### 2. validator.py - Validation Logic
**Responsibility**: Validates moves and checks solution correctness.

**Interfaces**:
- `validate_move(board, row, col, value):` Check if placing value at (row,col) is valid
- `is_complete(board):` Check if board has no empty cells
- `is_valid_solution(board):` Verify full solution correctness
- `check_conflicts(board, row, col):` Return list of conflicting cells

### 3. generator.py - Puzzle Generation
**Responsibility**: Generates valid Sudoku puzzles with different difficulty levels.

**Interfaces**:
- `generate_puzzle(difficulty='medium'):` Generate a new puzzle
  - Difficulty levels: 'easy', 'medium', 'hard', 'expert'
  - Returns tuple: (puzzle_with_holes, solution)
- `remove_numbers(full_board, holes):` Remove cells to create puzzle
- `solve_sudoku(board):` Backtracking solver for generating solutions

### 4. game.py - Game State Management
**Responsibility**: Manages the complete game state and rules enforcement.

**Interfaces**:
- `SudokuGame` class with:
  - `__init__(difficulty='medium'):` Create new game
  - `display():` Show current board state
  - `make_move(row, col, value):` Attempt to place a value
  - `check_mistakes():` Count and show current mistakes
  - `is_solved():` Check if game is completed correctly
  - `get_hint(row, col):` Provide a valid value for a cell
  - `solve():` Solve the entire puzzle

### 5. cli.py - Command Line Interface
**Responsibility**: User interaction via command line.

**Interfaces**:
- `main():` Main game loop
- `parse_command(input):` Parse player input
- Commands supported:
  - `move <row> <col> <value>` - Enter a number
  - `check` - Check current mistakes
  - `hint <row> <col>` - Get a hint
  - `solve` - Show solution
  - `new <difficulty>` - Start new game
  - `quit` - Exit game
  - `help` - Show help

### 6. main.py - Entry Point
**Responsibility**: Application startup.

**Interfaces**:
- `if __name__ == "__main__":` Entry point
  - Initializes game
  - Runs CLI loop
  - Handles graceful exit

## File Dependencies

```
main.py
    ↓
cli.py → game.py → board.py
                      ↓
                   validator.py
                      ↓
                   generator.py
```

## Data Flow

1. `main.py` starts and creates a `SudokuGame`
2. `cli.py` handles user input, parses commands
3. `SudokuGame` delegates board operations to `Board` class
4. `validate_move` in `validator.py` checks row/column/3x3 rules
5. `generator.py` creates puzzles using backtracking solver
6. Game tracks mistakes and completion status

## Constants

- GRID_SIZE = 9
- SUBGRID_SIZE = 3
- DIGITS = 1-9
- EMPTY = 0 or '.'
