import sys
import os
from random import randint, shuffle
from tile import Tile
from copy import deepcopy
from const import *
import utils

from time import time

class Game:
    __score = 0
    __startTiles = 2

    def __init__(self, verbose_flag=True):
        self.__board = {(i, j) : EMPTY
                        for i in range(BOARD_COLUMNS)
                        for j in range(BOARD_ROWS)}
        self.__verbose = verbose_flag
        self.__turn = Turn.PLAYER
        self.__gen_all_possible_moves = False
        self.__gen_all_possible_tiles = False

    def _gen_tile_at(self, place, number):
        self.__board[place] = Tile(number)

    def __get_empty_tiles(self):
        ''' Return list of empty tiles '''
        empty_tiles = []
        for pos, tile in self.__board.items():
            if tile == EMPTY:
                empty_tiles.append(pos)
        return empty_tiles

    def generate_tile(self, num_of_tiles=1):
        empty_tiles = self.__get_empty_tiles()
        shuffle(empty_tiles)
        for _ in range(0, num_of_tiles):
            if not empty_tiles:
                break
            else:
                pos = empty_tiles.pop()
                self.__board[pos] = Tile()
                self.__board[pos].set_random_value()
                # self.__score += self.__board[pos].get_value()
                self.__turn = Turn.PLAYER

        self.__gen_all_possible_moves = False
        self.__gen_all_possible_tiles = False

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
                self.__score += self.__board[curr_pos].get_value()*2
                self.__board[curr_pos] = EMPTY

    # Is the state is a final state
    def did_win(self):
        for curr_pos in filter(lambda x: self.__board[x] != EMPTY, TILES_UP_ORDER):
            if self.__board[curr_pos].get_value() == WINNING_THRESHOLD:
                return True
        return False

    def get_score(self):
        return self.__score

    def get_all_possible_tile_gen(self):
        start_time = time()
        if self.__gen_all_possible_moves:
            # print("---- %s seconds ----" %(time() - start_time))
            return self.__all_possible_moves

        current_state = deepcopy(self)
        current_state.__all_possible_moves = []
        current_state.__all_possible_tiles = []

        possible_tile_gen_list = []
        for pos in self.__get_empty_tiles():
            tmp_state = deepcopy(self)
            tmp_state.__turn = Turn.PLAYER
            tmp_state._gen_tile_at(pos, 2)
            possible_tile_gen_list.append((0.8/16, tmp_state))
            tmp_state._gen_tile_at(pos, 4)
            possible_tile_gen_list.append((0.2/16, tmp_state))

        self.__all_possible_moves = possible_tile_gen_list
        self.__gen_all_possible_moves = True
        endtime = time()
        # print ()
        return possible_tile_gen_list


    def get_all_possible_moves(self):
        start_time = time()
        if self.__gen_all_possible_tiles:
            # print("---- %s seconds ----" %(time() - start_time))
            return self.__all_possible_tiles

        current_state = deepcopy(self)
        current_state.__all_possible_moves = []
        current_state.__all_possible_tiles = []

        possible_moves = self.get_next_moves()
        states_after_moves_list = []
        for move in possible_moves:
            tmp_state = deepcopy(current_state)
            tmp_state.__turn = Turn.COMPUTER
            tmp_state.make_move(move)
            states_after_moves_list.append((move, tmp_state))
        self.__gen_possible_tiles = True
        self.__all_possible_tiles = states_after_moves_list
        # print("---- %s seconds ----" %(time() - start_time))
        return states_after_moves_list


    def get_board(self):
        ret_board = {}
        for pos in self.__board:
            if self.__board[pos] == EMPTY:
                ret_board[pos] = 0
            else:
                ret_board[pos] = self.__board[pos].get_value()
        return ret_board


    def get_next_moves(self):
        #TODO: add a cashe in order to not search twice per state
        moves = []
        for direction in DIRECTION_LIST:
            tiles_order = TILE_ORDER_DICT[direction]
            prev_func = utils.GET_PREV_DICT[direction]
            if self.__is_move_possible(tiles_order, prev_func):
                moves.append(direction)
        return moves

    def get_turn(self):
        return self.__turn


    def print_board(self):
        os.system('clear')
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
        self.__turn = Turn.COMPUTER
        self.__gen_all_possible_moves = False
        self.__gen_all_possible_tiles = False
        self.__all_possible_moves = []
        self.__all_possible_tiles = []

    def start_game_human(self):
        self.generate_tile(START_TILES)
        next_possibles_moves = self.get_next_moves()

        while next_possibles_moves:
            self.print_board()
            direction = sys.stdin.read(1)
            if direction not in DIRECTION_LIST or direction not in next_possibles_moves:
                continue
            self.make_move(direction)
            self.generate_tile()
            next_possibles_moves = self.get_next_moves()
        self.print_board()

if __name__ == '__main__':
    g = Game()
    g.start_game_human()
