from random import randint, shuffle
from const import *
import utils

class Tile:
    def __init__(self, value=0):
        self.__value = value
        self.__moved = False

    def set_value(self, value):
        self.__value = value

    def can_merge(self, tile):
        return self.__value == tile.get_value() and not self.__moved

    def merge(self, tile):
        self.__value *= 2
        self.__moved = true

    def get_value(self,tile):
        return self.__value

    def reset_tile_round_end(self):
        self.__moved = false

    def set_random_value(self):
        # Generate tile values
        tile_value = 2 if randint(1, 10) < 10 else 4
        self.__value = tile_value


class Game:
    __score = 0
    __startTiles = 2

    def __init__(self):
        self.__board = {(i, j) : EMPTY
                        for i in range(BOARD_COLUMNS)
                        for j in range(BOARD_ROWS)}

    def __get_empty_tiles(self):
        ''' Return list of empty tiles '''
        empty_tiles = []
        for pos, tile in self.__board.items():
            if tile == EMPTY:
                empty_tiles.append(pos)
        return empty_tiles

    def __generate_tile(self, num_of_tiles):
        empty_tiles = self.__get_empty_tiles()
        shuffle(empty_tiles)
        for _ in range(0, num_of_tiles):
            if not empty_tiles:
                break
            else:
                pos = empty_tiles.pop()
                self.__board[empty_tiles] = Tile()
                self.__board[empty_tiles].set_random_value()

    def __is_move_possible(self, tile_order, prev_tile_func, boundry_func):
        for curr_pos in tile_order:
            prev_pos = prev_tile_func(curr_pos)
            if self.__board[curr_pos] == EMPTY:
                continue
            if (boundry_func(*curr_pos) and
                    (self.__board[curr_pos] == self.__board[prev_pos] or
                     self.__board[prev_pos] == EMPTY)):
                return True
        return False

    def __find_farthest_pos(self, pos, get_prev_tile_f):
        prev_pos = get_prev_tile_f(pos)
        while (not utils.out_of_board(pos) and
               self.__board[pos] == EMPTY):
            pos = prev_pos
            prev_pos = get_prev_tile_f(prev_pos)
        return pos, prev_pos


    def __move_tiles(self, tiles_order, direction):

        get_prev_tile_f = utils.GET_PREV_DICT[direction]

        for curr_pos in filter(lambda x: self.__board[x] != EMPTY
                                    , tiles_order):
            farthest_pos, prev_farthest_pos = self.__find_farthest_pos(curr_pos,
                                                                get_prev_tile_f)
            if pos == farthest_pos:
                continue
            elif self.__board[farthest_pos] == EMPTY:
                self.__board[farthest_pos], self.__board[curr_pos] = \
                self.__board[curr_pos], self.__board[farthest_pos]
            elif self.__board[farthest_pos].can_merge(self.__board[curr_pos]):
                self.__board[farthest_pos].merge(self.__board[curr_pos])
                self.__board[curr_pos] = EMPTY
            else:
                self.__board[prev_farthest_pos] = self.__board[curr_pos]
                self.__board[curr_pos] = EMPTY

    def return_board(self):
        return self.__board

    def get_next_moves(self):
        moves = []
        if self.__is_move_possible(TILES_UP_ORDER, utils.get_prev_tile_up,
                                   utils.is_boundry_up):
            moves.append(UP)
        if self.__is_move_possible(TILES_RIGHT_ORDER, utils.get_prev_tile_right,
                                   utils.is_boundry_right):
            moves.append(RIGHT)
        if self.__is_move_possible(TILES_DOWN_ORDER, utils.get_prev_tile_down,
                                   utils.is_boundry_down):
            moves.append(DOWN)
        if self.__is_move_possible(TILES_LEFT_ORDER, utils.get_prev_tile_left,
                                   utils.is_boundry_left):
            moves.append(LEFT)
        return moves

    def make_move(self, direction):
        tiles_order = TILE_ORDER_DICT[direction]
        self.__move_tiles(tiles_order, direction)
        for pos in filter(lambda pos: self.__board[pos] != EMPTY, tile_order):
            self.__board[pos].reset_tile_round_end()

    def start_game(self):
        self.__generate_tile(START_TILES)
