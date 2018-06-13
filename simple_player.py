from abstract_player import AbstractPlayer
from const import DIRECTION_LIST
from expectimax import Expectimax
from time import sleep
from cost_functions import weighted_spots

class SimplePlayer(AbstractPlayer):

    def __init__(self, f_no_more_time, max_depth, delay=0):
        self.__expectimax = Expectimax(f_no_more_time)
        self.__max_depth = max_depth
        self.__delay = delay

    def get_move(self, state):
        all_possible_moves = state.get_all_possible_moves()
        best_move = None
        best_score = 0

        for move, next_state in all_possible_moves:
            score = self.__expectimax.search(next_state, self.__max_depth, weighted_spots)
            if score >= best_score:
                best_move = move
                best_score = score

        if self.__delay:
            sleep(self.__delay)
        return best_move
