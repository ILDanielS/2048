from random import randint, shuffle
from const import *
import utils
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
        for pos, value in self.__board.items():
            if value == EMPTY:
                empty_tiles.append(pos)
        return empty_tiles

    def __generate_tile(self, num_of_tiles):
        empty_tiles = self.__get_empty_tiles()
        shuffle(empty_tiles)

        for _ in range(0, num_of_tiles):
            if not empty_tiles:
                break
            else:
                # Generate tile values
                tile_value = 2 if randint(1, 10) < 10 else 4
                self.__board[empty_tiles.pop()] = tile_value

    def __is_move_possible(self, tile_order, prev_tile_func, boundry_func):
        for curr_pos in tile_order:
            prev_pos = prev_tile_func(curr_pos)
            if self.__board[curr_pos] == 0:
                continue
            if (boundry_func(curr_pos) and
                    (self.__board[curr_pos] == self.__board[prev_pos] or
                     self.__board[prev_pos] == 0)):
                return True
        return False

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

    def start_game(self):
        self.__generate_tile(START_TILES)
