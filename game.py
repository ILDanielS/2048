import sys
import os
from random import randint, shuffle
from tile import Tile
from copy import deepcopy
from const import *
import utils

class Game:
    __score = 0
    __startTiles = 2

    def __init__(self, verbose_flag=True):
        self.__board = {(i, j) : EMPTY
                        for i in range(BOARD_COLUMNS)
                        for j in range(BOARD_ROWS)}
        self.__verbose = verbose_flag
        self.__turn = PLAYER

    def _gen_tile_at(self, place, number):
        self.__board[place] = Tile(number)

    def __get_empty_tiles(self):
        ''' Return list of empty tiles '''
        empty_tiles = []
        for pos, tile in self.__board.items():
            if tile == EMPTY:
                empty_tiles.append(pos)
        return empty_tiles

    def __generate_tile(self, num_of_tiles=1):
        empty_tiles = self.__get_empty_tiles()
        shuffle(empty_tiles)
        for _ in range(0, num_of_tiles):
            if not empty_tiles:
                break
            else:
                pos = empty_tiles.pop()
                self.__board[pos] = Tile()
                self.__board[pos].set_random_value()

    def __is_move_possible(self, tile_order, prev_tile_func):
        for curr_pos in filter(lambda x: self.__board[x] != EMPTY, tile_order):
            far_pos, pre_far_pos = self.__find_farthest_pos(curr_pos, prev_tile_func)
            is_out_bound = utils.out_of_board(far_pos)
            can_move = pre_far_pos != curr_pos
            # pdb.set_trace()
            if can_move or \
            not is_out_bound and \
            self.__board[curr_pos].can_merge(self.__board[far_pos]):
                return True
        return False

    def __find_farthest_pos(self, pos, get_prev_tile_f):
        prev_pos = pos
        pos = get_prev_tile_f(*pos)
        while not utils.out_of_board(pos) and self.__board[pos] == EMPTY:
            prev_pos, pos = pos, get_prev_tile_f(*pos)
        return pos, prev_pos

    def __move_tiles(self, tiles_order, direction):
        get_prev_tile_f = utils.GET_PREV_DICT[direction]
        for curr_pos in filter(lambda x: self.__board[x] != EMPTY
                               , tiles_order):
            # pdb.set_trace()
            farthest_pos, prev_farthest_pos = \
                                    self.__find_farthest_pos(curr_pos,
                                                             get_prev_tile_f)
            if (utils.out_of_board(farthest_pos) or
            not self.__board[farthest_pos].can_merge(self.__board[curr_pos])):
                self.__board[curr_pos], self.__board[prev_farthest_pos] = \
                                          EMPTY, self.__board[curr_pos]
            else:
                self.__board[farthest_pos].merge()
                self.__board[curr_pos] = EMPTY

    # Is the state is a final state
    def did_win(self):
        for curr_pos in filter(lambda x: self.__board[x] != EMPTY, tiles_order):
            if self.__board[curr_pos].get_value() == WINNING_THRESHOLD:
                return True
        return False

    def get_all_possible_tile_gen(self):
        current_board = deepcopy(self.__board)
        tmp_board = deepcopy(self.__board)
        all_possible_tile_gen_list = []
        empty_tiles_pos = self.__get_empty_tiles()
        for pos in empty_tiles_pos:
            tmp_board[pos] = Tile(2)
            all_possible_tile_gen_list.append((0.8, tmp_board))
            tmp_board[pos].set_value(4)
            all_possible_tile_gen_list.append((0.2, tmp_board))
            tmp_board = deepcopy(current_board)

        return all_possible_tile_gen_list

    def get_all_possible_moves(self):
        possible_moves = self.get_next_moves()
        boards_after_moves = []
        tmp_board = deepcopy(self.__board)
        for move in possible_moves:
            tmp_board.make_move(move)
            boards_after_moves.append((move, tmp_board))
            tmp_board = deepcopy(self.__board)
        return boards_after_moves

    def return_board(self):
        return self.__board

    def get_next_moves(self):
        moves = []
        for direction in DIRECTION_LIST:
            tiles_order = TILE_ORDER_DICT[direction]
            prev_func = utils.GET_PREV_DICT[direction]
            if self.__is_move_possible(tiles_order, prev_func):
                moves.append(direction)
        return moves

    def print_board(self):
        os.system('cls')
        print('-'*BOARD_COLUMNS*5)
        for (i, j) in TILES_UP_ORDER:
            if self.__board[(i, j)] == EMPTY:
                print(repr(0).rjust(4), end="|")
            else:
                print(repr(self.__board[(i, j)].get_value()).rjust(4), end="|")
            if j+1 == BOARD_COLUMNS:
                print("\n"+'-'*BOARD_COLUMNS*5)

    def make_move(self, direction):
        tiles_order = TILE_ORDER_DICT[direction]
        self.__move_tiles(tiles_order, direction)
        for pos in filter(lambda pos: self.__board[pos] != EMPTY, tiles_order):
            self.__board[pos].reset_tile_round_end()

    def start_game_human(self):
        self.__generate_tile(START_TILES)

        next_possibles_moves = self.get_next_moves()
        while next_possibles_moves:
            self.print_board()
            direction = sys.stdin.read(1)
            if direction not in DIRECTION_LIST or direction not in next_possibles_moves:
                continue
            self.make_move(direction)
            self.__generate_tile()
            next_possibles_moves = self.get_next_moves()
        self.print_board()

if __name__ == '__main__':
    g = Game()
    g.start_game_human()
