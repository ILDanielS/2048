# from copy import deepcopy
from const import Turn

class Expectimax:
    def __init__(self, f_no_more_time):
        """ Initialize expectimax algorithm
            :param f_no_more_time - A functino that returns true if there is no
                                    more time to run this search
        """
        self.f_no_more_time = f_no_more_time

    def search(self, state, depth, score_func):
        """ Start the expectimax algorithm
            :param: state - Game instance of the current state
            :param: depth - the maximum depth to go
            :param: score_func - Heuristic functnion for state score
            :return: return the best score that can be achived
        """

        turn = state.get_turn()

        if self.f_no_more_time() or depth <= 0:
            return score_func(state)
        if state.get_turn() == Turn.COMPUTER:
            prob_sum = 0
            possible_gen_list = state.get_all_possible_tile_gen()
            for (prob, next_state) in possible_gen_list:
                prob_sum += prob * self.search(next_state, depth - 1, score_func)
            return sum

        next_moves = state.get_all_possible_moves()

        if not next_moves:
            return score_func(state)

        best_score = 0

        for next_move, next_state in next_moves:
            tmp_score = self.search(next_state, depth-1, score_func)
            if tmp_score > best_score:
                selected_move = next_move
                best_score = tmp_score

        return best_score
