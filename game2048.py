import random

class Game2048:
    __board = []
    __score = 0
    __startTiles = 2

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


    def __get_empty_tiles(self):
        empty_tiles = []
        for i in range(0,4):
            for j in range(0,4):
                if self.__board[i][j] == 0:
                    empty_tiles.append((i,j))
        return empty_tiles


    def __generate_tile(self, iteration):
        for _ in range(0, iteration):
            # generate a 2 tile or a 4 tile
            rand_tile_num = 2 if random.randint(1,10) < 10 else 4
            empty_tiles = self.__get_empty_tiles()
            i,j = random.choice(empty_tiles)
            self.__board[i][j] = rand_tile_num


    def start_game(self):
        self.__generate_tile(self.__startTiles)


g = Game2048()
g.start_game()

print(g.print_board())
