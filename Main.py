from Game import *
from Human import *
from Artificial_Intelligence import *





def main():
    game = Game()
    game.window()
    choise = game.mode_choise()
    if choise == "1":
        game.game(Human(),Human())
    elif choise == "2":
        game.game(Human(),Artificial_Intelligence())
    else:
        game.game(Artificial_Intelligence(),Artificial_Intelligence())



if __name__ == "__main__":
    main()
    pass
    