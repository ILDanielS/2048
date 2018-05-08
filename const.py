''' Consts and some more definitions to use in game module '''
# Board setup
EMPTY = None
BOARD_ROWS = 4
BOARD_COLUMNS = 4
START_TILES = 2

# Moves
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

TILES_UP_ORDER = [(x, y) for x in range(BOARD_ROWS)
                  for y in range(BOARD_COLUMNS)]

TILES_RIGHT_ORDER = [(x, y) for y in reversed(range(BOARD_COLUMNS))
                     for x in range(BOARD_ROWS)]

TILES_DOWN_ORDER = [(x, y) for x in reversed(range(BOARD_ROWS))
                    for y in reversed(range(BOARD_COLUMNS))]

TILES_LEFT_ORDER = [(x, y) for y in range(BOARD_COLUMNS)
                    for x in reversed(range(BOARD_ROWS))]
