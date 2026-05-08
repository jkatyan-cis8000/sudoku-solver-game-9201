from board import GRID_SIZE, SUBGRID_SIZE, EMPTY


def _get_row(board, row):
    return board.grid[row]


def _get_column(board, col):
    return [board.grid[row][col] for row in range(GRID_SIZE)]


def _get_subgrid(board, row, col):
    start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
    start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE
    cells = []
    for r in range(start_row, start_row + SUBGRID_SIZE):
        for c in range(start_col, start_col + SUBGRID_SIZE):
            cells.append(board.grid[r][c])
    return cells


def validate_move(board, row, col, value):
    if value == EMPTY:
        return True
    
    if not (1 <= value <= 9):
        return False
    
    if board.get_cell(row, col) != EMPTY:
        return False
    
    row_cells = _get_row(board, row)
    if value in row_cells:
        return False
    
    col_cells = _get_column(board, col)
    if value in col_cells:
        return False
    
    subgrid_cells = _get_subgrid(board, row, col)
    if value in subgrid_cells:
        return False
    
    return True


def is_complete(board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board.get_cell(row, col) == EMPTY:
                return False
    return True


def is_valid_solution(board):
    if not is_complete(board):
        return False
    
    target = set(range(1, 10))
    
    for row in range(GRID_SIZE):
        if set(_get_row(board, row)) != target:
            return False
    
    for col in range(GRID_SIZE):
        if set(_get_column(board, col)) != target:
            return False
    
    for start_row in range(0, GRID_SIZE, SUBGRID_SIZE):
        for start_col in range(0, GRID_SIZE, SUBGRID_SIZE):
            cells = []
            for r in range(start_row, start_row + SUBGRID_SIZE):
                for c in range(start_col, start_col + SUBGRID_SIZE):
                    cells.append(board.grid[r][c])
            if set(cells) != target:
                return False
    
    return True


def check_conflicts(board, row, col):
    conflicts = []
    value = board.get_cell(row, col)
    
    if value == EMPTY:
        return conflicts
    
    for i in range(GRID_SIZE):
        if i != col and board.get_cell(row, i) == value:
            conflicts.append((row, i))
    
    for i in range(GRID_SIZE):
        if i != row and board.get_cell(i, col) == value:
            conflicts.append((i, col))
    
    start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
    start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE
    for r in range(start_row, start_row + SUBGRID_SIZE):
        for c in range(start_col, start_col + SUBGRID_SIZE):
            if (r != row or c != col) and board.get_cell(r, c) == value:
                conflicts.append((r, c))
    
    return conflicts
