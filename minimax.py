from const import Turn, INFTY


class Minimax:
    def __init__(self, score_func):
        self.__score_func = score_func

    def search(self, state, depth, alpha, beta):
        turn = state.get_turn()
        if depth == 0:
            return self.__score_func(state)

        if turn == Turn.PLAYER:
            possible_moves_list = state.get_all_possible_moves()
            if not possible_moves_list:
                return self.__score_func(state)
            max_score = -INFTY
            for _, next_state in possible_moves_list:
                curr_score = self.search(next_state, depth-1, alpha, beta)
                max_score = max(curr_score, max_score)
                alpha = max(max_score, alpha)
                if max_score >= beta:
                    return INFTY
            return max_score

        elif turn == Turn.COMPUTER:
            possible_gen_list = state.get_all_possible_tile_gen()
            if not possible_gen_list:
                return self.__score_func(state)
            min_score = INFTY
            for _, next_state in possible_gen_list:
                current_score = self.search(next_state, depth-1, alpha, beta)
                min_score = min(current_score, min_score)
                beta = min(min_score, beta)
                if min_score <= alpha:
                    return -INFTY
            return min_score
