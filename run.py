from human_player import HumanPlayer
from manager_console import ConsoleManager

if __name__ == '__main__':
    human = HumanPlayer()
    game = ConsoleManager(human)
    game.start_game()
