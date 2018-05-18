from const import BOARD_ROWS, BOARD_COLUMNS, UP, RIGHT, DOWN, LEFT
# UP move functinos
def get_prev_tile_up(i, j):
    return (i-1, j)
def is_boundry_up(i, j):
    return i >= 0
def start_of_line_up(i, j):
    return 0, j

# RIGHT move functions
def get_prev_tile_right(i, j):
    return (i, j+1)
def is_boundry_right(i, j):
    return j <= BOARD_COLUMNS - 1
def start_of_line_right(i, j):
    return (i, BOARD_COLUMNS - 1)

# DOWN move functions
def get_prev_tile_down(i, j):
    return (i+1, j)
def is_boundry_down(i, j):
    return i <= BOARD_ROWS - 1
def start_of_line_down(i, j):
    return (BOARD_ROWS, j)

# LEFT move functnions
def get_prev_tile_left(i, j):
    return (i, j-1)
def is_boundry_left(i, j):
    return j >= 0
def start_of_line_left(i, j):
    return (i, 0)

# Dictionaries
GET_PREV_DICT = {UP: get_prev_tile_up,
                 LEFT: get_prev_tile_left,
                 DOWN: get_prev_tile_down,
                 RIGHT: get_prev_tile_right
                }

def out_of_board(pos):
    i, j = pos
    return (i >= BOARD_ROWS or
            i < 0 or
            j >= BOARD_COLUMNS or
            j < 0)
