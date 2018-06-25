from const import TILES_UP_ORDER, TILES_RIGHT_ORDER, BOARD_COLUMNS, BOARD_ROWS

def smoothness_rows(board):
    diff = 0
    for i,j in TILES_UP_ORDER:
        if j == BOARD_COLUMNS-1 or not board[(i,j)] or not board[(i,j+1)]:
            continue
        diff += abs(board[(i,j)] - board[(i,j+1)])

    return diff


def smoothness_columns(board):
    diff = 0
    for i,j in TILES_RIGHT_ORDER:
        if i == BOARD_ROWS-1 or not board[(i,j)] or not board[(i+1, j)]:
            continue
        diff += abs(board[(i, j)] - board[(i+1, j)])

    return diff


def smoothness(board):
    return -1*(smoothness_rows(board) + smoothness_columns(board))

def game_score(state):
    return state.get_score()

def weighted_value(state):
    score = game_score(state)
    smooth = smoothness(state)
    return score + smooth*2000


def weighted_spots(board):
    # board = state.get_board()
    base = 3
    magnitute = [16,15,14,13,9,10,11,12,8,7,6,5,1,2,3,2,1]
    score = 0
    for i in range(16):
        pos = TILES_UP_ORDER[i]
        score += board[pos]*(base**magnitute[i])
    return score

def free_tiles(board):
    score = 0
    max_tile = 0
    # board = state.get_board()
    for pos in board:
        if not board[pos]:
            score += 3**10
        else:
            max_tile = max(max_tile, board[pos])
    return score*max_tile

def monotocity(board):
    score = 0
    base = 2
    magnitute = [11,10,9,8, 10,9,8,7, 9,8,7,6, 8,7,6,5]
    for i in range(16):
        pos = TILES_UP_ORDER[i]
        score += board[pos]*(base**magnitute[i])
    return score

def heuristic(state):
    board = state.get_board()

    return free_tiles(board) + weighted_spots(board) #monotocity(board)
