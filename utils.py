from const import BOARD_ROWS, BOARD_COLUMNS
# UP move functinos
def get_prev_tile_up(i, j):
    return (i-1, j)
def is_boundry_up(i, j):
    return i == 0

# RIGHT move functions
def get_prev_tile_right(i, j):
    return (i, j+1)
def is_boundry_right(i, j):
    return j == BOARD_COLUMNS - 1

# DOWN move functions
def get_prev_tile_down(i, j):
    return (i+1, j)
def is_boundry_down(i, j):
    return i == BOARD_ROWS - 1

# LEFT move functnions
def get_prev_tile_left(i, j):
    return (i, j-1)
def is_boundry_left(i, j):
    return j == 0
