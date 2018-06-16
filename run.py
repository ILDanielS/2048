from human_player import HumanPlayer
from simple_player import SimplePlayer
from minimax_player import MinimaxPlayer
from manager_console import ConsoleManager

if __name__ == '__main__':
    player = MinimaxPlayer(0, 0.25)
    game = ConsoleManager(player)
    game.start_game()
