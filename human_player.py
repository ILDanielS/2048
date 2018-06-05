from abstract_player import AbstractPlayer
from const import DIRECTION_LIST
from sys import stdin
class HumanPlayer(AbstractPlayer):

    def __init__(self):
        pass

    def get_move(self):
        direction = stdin.read(1)
        while direction not in DIRECTION_LIST:
            direction = stdin.read(1)
        return direction
