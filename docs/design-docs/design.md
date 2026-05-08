# Sudoku Game Design Documentation

## board.py - Board Management

### Purpose
Manages the 9x9 Sudoku grid, provides basic operations for cell access, string representation, and copying.

### Key Components
- **Constants**: `GRID_SIZE=9`, `SUBGRID_SIZE=3`, `EMPTY=0`
- **Board Class**: Core data structure for the puzzle grid

### Interface
- `__init__()`: Creates empty 9x9 grid initialized with zeros
- `set_cell(row, col, value)`: Sets the value at a specific cell
- `get_cell(row, col)`: Retrieves the value at a specific cell
- `to_string()`: Returns formatted string with subgrid separators (| and -)
- `copy()`: Creates deep copy of the board

### Design Decisions
- Uses 0 to represent empty cells (consistent with Sudoku conventions)
- String representation includes visual subgrid boundaries for CLI display
- Deep copy ensures board mutations don't affect original

## validator.py - Validation Logic

### Purpose
Validates moves against Sudoku rules and checks solution correctness.

### Key Components
- Row, column, and 3x3 subgrid extraction helpers
- Conflict detection mechanism

### Interface
- `validate_move(board, row, col, value)`: Checks if placing value violates rules
- `is_complete(board)`: Verifies no empty cells remain
- `is_valid_solution(board)`: Full solution validation (all rows, columns, subgrids contain 1-9)
- `check_conflicts(board, row, col)`: Returns list of conflicting cell coordinates

### Design Decisions
- Validation checks three constraints: row uniqueness, column uniqueness, subgrid uniqueness
- Empty cells don't cause conflicts
- Returns full conflict list for potential UI highlighting

## generator.py - Puzzle Generation

### Purpose
Generates valid Sudoku puzzles with configurable difficulty levels.

### Key Components
- Backtracking solver for generating complete solutions
- Random cell removal for creating puzzles

### Interface
- `generate_puzzle(difficulty)`: Creates puzzle and solution tuple
- `remove_numbers(full_board, holes)`: Removes cells to create puzzle
- `solve_sudoku(board)`: Solves board using backtracking

### Difficulty Levels
- easy: 30 holes
- medium: 40 holes
- hard: 50 holes
- expert: 60 holes

### Design Decisions
- Generates full valid board first, then removes cells
- Random shuffling of cell removal order prevents patterns
- Backtracking ensures solution exists

## game.py - Game State Management

### Purpose
Manages complete game state including board, difficulty, and mistake tracking.

### Key Components
- SudokuGame class with full game lifecycle

### Interface
- `__init__(difficulty)`: Creates new game with puzzle generation
- `display()`: Shows board and mistake count
- `make_move(row, col, value)`: Attempts move, tracks mistakes
- `check_mistakes()`: Returns mistake count
- `is_solved()`: Checks if puzzle is correctly solved
- `get_hint(row, col)`: Provides solution value for cell
- `solve()`: Reveals full solution

### Design Decisions
- Distinguishes between initial (immutable) and puzzle board
- Mistakes tracked for incorrect moves only
- Hint system uses pre-computed solution

## cli.py - Command Line Interface

### Purpose
Handles user interaction via text-based commands.

### Key Components
- Command parsing and dispatch system
- Game loop with prompt

### Supported Commands
- `move <row> <col> <value>`: Enter number (0-indexed rows/cols)
- `check`: Show mistake count
- `hint <row> <col>`: Get value for cell
- `solve`: Reveal solution
- `new <difficulty>`: Start new game
- `quit`: Exit application
- `help`: Display command reference
- `display`: Refresh board view

### Design Decisions
- Zero-indexed for consistency with Python conventions
- Input validation for all parameters
- Graceful error messages for invalid inputs

## main.py - Entry Point

### Purpose
Application startup and main game loop initialization.

### Key Components
- Imports cli module and runs main function

### Design Decisions
- Simple entry point that delegates to cli module
- Standard Python `if __name__ == "__main__"` pattern

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

1. Application starts in `main.py`
2. `cli.py` creates `SudokuGame` instance
3. `SudokuGame` uses `generator.py` to create puzzle
4. `generator.py` uses `solve_sudoku()` which calls `validate_move()` from `validator.py`
5. Player moves through `cli.py` call `make_move()` in `game.py`
6. `make_move()` validates using `validator.py` and updates board in `board.py`
7. Game state persists across interactions until completion
