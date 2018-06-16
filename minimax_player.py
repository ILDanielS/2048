from time import sleep
from minimax import Minimax
from cost_functions import weighted_spots, heuristic
from const import INFTY

class MinimaxPlayer:
    def __init__(self, max_depth, time):
        self.__minimax = Minimax(heuristic)
        self.__max_depth = max_depth
        self.__time = time
        # self.__delay = delay

    def get_move(self, state):
        # all_possible_moves = state.get_all_possible_moves()
        # best_move = None
        # best_score = 0
        #
        # for move, next_state in all_possible_moves:
        #     score = self.__minimax.search(next_state, self.__max_depth-1, -INFTY, INFTY)
        #     if score >= best_score:
        #         best_move = move
        #         best_score = score
        #
        # if self.__delay:
        #     sleep(self.__delay)
        # return best_move
        return self.get_move_iterative(state)

    def get_move_iterative(self, state):
        return self.__minimax.iterative_deepening(state, self.__time, True)
