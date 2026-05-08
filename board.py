GRID_SIZE = 9
SUBGRID_SIZE = 3
EMPTY = 0


class Board:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    def set_cell(self, row, col, value):
        self.grid[row][col] = value

    def get_cell(self, row, col):
        return self.grid[row][col]

    def to_string(self):
        lines = []
        for i, row in enumerate(self.grid):
            row_str = []
            for j, cell in enumerate(row):
                if j > 0 and j % SUBGRID_SIZE == 0:
                    row_str.append("|")
                if cell == EMPTY:
                    row_str.append(".")
                else:
                    row_str.append(str(cell))
            lines.append(" ".join(row_str))
            if i > 0 and i % SUBGRID_SIZE == 0:
                lines.append("---+---+---")
        return "\n".join(lines)

    def copy(self):
        new_board = Board()
        new_board.grid = [row[:] for row in self.grid]
        return new_board

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.grid == other.grid
