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

    def board_up(self):
        walls_positions = [-1]*4

        for i in range (0,4):
            for j in range(0,4):
                wall_i = walls_positions[j]
                if self.__board[i][j] == 0:
                    continue
                if (wall_i == -1
                    or self.__board[i][j] != self.__board[wall_i][j]):
                    tile_value = self.__board[i][j]
                    self.__board[i][j] = 0
                    self.__board[wall_i+1][j] = tile_value
                    walls_positions[j] = i
                else:
                    self.__board[wall_i][j] *=2
                    self.__board[i][j] = 0


    def start_game(self):
        self.__generate_tile(self.__startTiles)


    def print_board(self):
        for i in range (0,4):
            for j in range (0,4):
                print(self.__board[i][j], end=" ")
            print("\n")


g = Game2048()
g.start_game()
g.print_board()
print('-'*8, end="\n")
g.board_up()
g.print_board()
# print(g.print_board())
