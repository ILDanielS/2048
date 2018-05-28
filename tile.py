class Tile:
    def __init__(self, value=0):
        self.__value = value
        self.__moved = False

    def set_value(self, value):
        self.__value = value

    def can_merge(self, tile):
        return self.__value == tile.get_value() and not self.__moved

    def merge(self):
        self.__value *= 2
        self.__moved = True

    def get_value(self):
        return self.__value

    def reset_tile_round_end(self):
        self.__moved = False

    def set_random_value(self):
        # Generate tile values
        tile_value = 2 if randint(1, 10) < 10 else 4
        self.__value = tile_value
