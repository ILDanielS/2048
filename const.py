''' Consts and some more definitions to use in game module '''
# Board setup
EMPTY = None
BOARD_ROWS = 4
BOARD_COLUMNS = 4
START_TILES = 2

WINNING_THRESHOLD = 2048

# Moves
UP = 'w'
RIGHT = 'd'
DOWN = 's'
LEFT = 'a'
DIRECTION_LIST = [UP, RIGHT, DOWN, LEFT]
# Keyboard character to direction

TILES_UP_ORDER = [(x, y) for x in range(BOARD_ROWS)
                  for y in range(BOARD_COLUMNS)]

TILES_RIGHT_ORDER = [(x, y) for y in reversed(range(BOARD_COLUMNS))
                     for x in range(BOARD_ROWS)]

TILES_DOWN_ORDER = [(x, y) for x in reversed(range(BOARD_ROWS))
                    for y in reversed(range(BOARD_COLUMNS))]

TILES_LEFT_ORDER = [(x, y) for y in range(BOARD_COLUMNS)
                    for x in reversed(range(BOARD_ROWS))]


# Dictionaries for easy access
TILE_ORDER_DICT = {UP: TILES_UP_ORDER,
                   RIGHT: TILES_RIGHT_ORDER,
                   DOWN: TILES_DOWN_ORDER,
                   LEFT: TILES_LEFT_ORDER}
