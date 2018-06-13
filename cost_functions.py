from const import TILES_UP_ORDER, TILES_RIGHT_ORDER, BOARD_COLUMNS, BOARD_ROWS

def smoothness_rows(board):
    plus_signs = 0
    minus_signs = 0

    for i,j in TILES_UP_ORDER:
        if j == BOARD_COLUMNS-1:
            continue
        diff = board[(i,j)] - board[(i,j+1)]
        if diff > 0:
            plus_signs += 1
        elif diff < 0:
            minus_signs += 1

    return abs(plus_signs - minus_signs)


def smoothness_columns(board):
    plus_signs = 0
    minus_signs = 0

    for i,j in TILES_RIGHT_ORDER:
        if i == BOARD_ROWS-1:
            continue
        diff = board[(i, j)] - board[(i+1, j)]
        if diff > 0:
            plus_signs += 1
        elif diff < 0:
            minus_signs += 1

    return abs(plus_signs - minus_signs)


def smoothness(state):
    board = state.get_board()
    return -1*max(smoothness_rows(board), smoothness_columns(board))

def game_score(state):
    return state.get_score()

def weighted_value(state):
    score = game_score(state)
    smooth = smoothness(state)
    return score + smooth*2000


def weighted_spots(state):
    board = state.get_board()
    exp = 4
    magnitute = [16,15,14,13,9,10,11,12,8,7,6,5,1,2,3,2,1]
    score = 0
    for i in range(16):
        pos = TILES_UP_ORDER[i]
        score += board[pos]*(magnitute[i]**exp)
    return score
