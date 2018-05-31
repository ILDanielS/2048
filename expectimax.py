from copy import deepcopy

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

        if turn == Turn.COMPUTER:
            sum = 0
            possible_gen_list = state.get_all_possible_tile_gen()
            for (prob, next_state) in possible_gen_list:
                sum += prob * this.search(next_state, depth - 1)
            return sum

        next_moves = state.get_all_possible_moves()

        if not next_moves:
            return score_func(state)

        selected_move = next_moves[0]
        best_score = 0

        for next_move, next_state in next_moves:
            tmp_score = search(next_state, depth-1)
            if tmp_score > best_score:
                selected_move = next_move
                best_score = tmp_score

        return best_score
