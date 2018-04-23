import random

class Game2048:
    __board = []
    __score = 0

    def __init__(self):
        for i in range (0,4):
            self.__board.append([])
            for j in range (0,4):
                self.__board[i].append(0)

    def print_board(self):
        for i in range (0,4):
            for j in range (0,4):
                print(self.__board[i][j], end=" ")
            print("\n")

    def start_game(self):
        random


g = Game2048()

print(g.print_board())
