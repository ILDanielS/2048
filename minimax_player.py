from time import sleep
from minimax import Minimax
from cost_functions import weighted_spots
from const import INFTY

class MinimaxPlayer:
    def __init__(self, max_depth, delay=0):
        self.__minimax = Minimax(weighted_spots)
        self.__max_depth = max_depth
        self.__delay = delay

    def get_move(self, state):
        all_possible_moves = state.get_all_possible_moves()
        best_move = None
        best_score = 0

        for move, next_state in all_possible_moves:
            score = self.__minimax.search(next_state, self.__max_depth-1, -INFTY, INFTY)
            if score >= best_score:
                best_move = move
                best_score = score

        if self.__delay:
            sleep(self.__delay)
        return best_move
