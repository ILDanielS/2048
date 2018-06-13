import os
import game as g
import const

class ConsoleManager:

    def __init__(self, player):
        self.__state = g.Game()
        self.__player = player

    def print_board(self):
        board = self.__state.get_board()
        os.system('clear')
        print('*** Score:', self.__state.get_score(), '***')
        print('-'*const.BOARD_COLUMNS*5)
        for (i, j) in const.TILES_UP_ORDER:
            print(repr(board[(i, j)]).rjust(4), end="|")
            if j+1 == const.BOARD_COLUMNS:
                print("\n"+'-'*const.BOARD_COLUMNS*5)


    def start_game(self):
        self.__state.generate_tile(const.START_TILES)
        next_possibles_moves = self.__state.get_next_moves()
        while next_possibles_moves:
            self.print_board()
            direction = self.__player.get_move(self.__state)
            if direction not in const.DIRECTION_LIST or \
               direction not in next_possibles_moves:
                continue
            self.__state.make_move(direction)
            self.__state.generate_tile()
            next_possibles_moves = self.__state.get_next_moves()
        self.print_board()
