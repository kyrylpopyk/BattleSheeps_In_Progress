from Game import *
from Human import *
from Artificial_Intelligence import *


if sys.platform.lower() == "win32": 
    os.system('color')

def mode_choise():
    Global().wizard_talking(f"Hi, I am a {Global.wizard_name}. The great wizard!")
    Global().wizard_talking("Сhoose how you want to play")
    print("\n(1) - Human VS Human\n(2) - Human VS AI(In progress)\n(3) - AI VS AI(In progress)")
    user_input = ""
    while user_input != "1" and user_input != "2" and user_input != "3":
        user_input = Global().check_input("\nCommand - ")
    return user_input


def main():
    choise = mode_choise()
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

    