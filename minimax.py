from const import Turn, INFTY
from time import time


class Minimax:
    def __init__(self, score_func, timer):
        self.__score_func = score_func
        self.__timer = timer

    def search(self, state, depth, alpha, beta):
        turn = state.get_turn()
        if depth == 0:
            return self.__score_func(state)

        if turn == Turn.PLAYER:
            possible_moves_list = state.get_all_possible_moves()
            if not possible_moves_list:
                # return self.__score_func(state) if state.have_2048() else -INFTY
                return -INFTY
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
                # return self.__score_func(state) if state.have_2048() else -INFTY
                return -INFTY
            min_score = INFTY
            for prob, next_state in possible_gen_list:
                if prob == 0.2/16:
                    continue
                current_score = self.search(next_state, depth-1, alpha, beta)
                min_score = min(current_score, min_score)
                beta = min(min_score, beta)
                if min_score <= alpha:
                    return -INFTY
            return min_score

    def iterative_deepening(self, state, verbose_flag):
        # start_time = time()
        self.__timer.start_timer()
        depth = 1
        all_possible_moves = state.get_all_possible_moves()

        best_move = None
        best_score = 0

        while(True):
            if verbose_flag:
                print("Reached", depth, "level")

            for move, next_state in all_possible_moves:
                score = self.search(next_state, depth-1, -INFTY, INFTY)
                if score >= best_score:
                    best_move = move
                    best_score = score

            # if time() - start_time >= run_time:
            #     break
            if self.__timer.is_over():
                break

            depth += 1

        return best_move
