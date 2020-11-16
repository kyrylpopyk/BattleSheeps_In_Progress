from Game import *
from Human import *
from Artificial_Intelligence import *


if sys.platform.lower() == "win32": 
    os.system('color')

def mode_choise(self):
        self.wizard_talking(f"Hi, I am a {self.wizard_name}. The great wizard!")
        self.wizard_talking("Сhoose how you want to play")
        print("\n(1) - Human VS Human\n(2) - Human VS AI\n(3) - AI VS AI")
        user_input = ""
        while user_input != "1" and user_input != "2" and user_input != "3":
            user_input = self.check_input("\nCommand - ")
        return user_input


def main():
    choise = "2"#mode_choise() test
    game = Game()
    if choise == "1":
        game.game(Human(game.board_size), Human(game.board_size))
    elif choise == "2":
        game.game(Human(game.board_size), Artificial_Intelligence(game.board_size))
    elif choise == "3":
        game.game(Artificial_Intelligence(game.board_size), Artificial_Intelligence(game.board_size))



if __name__ == "__main__":
    main()
    pass

    