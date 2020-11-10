from Global import *
from Inteligence import *

class Game(Global):
    player_1 = Inteligence()
    player_2 = Inteligence()
    board = []

    def window(self):
        os.system('mode con: cols=100 lines=25')
    
    def game(self, player_1 = Inteligence,player_2 = Inteligence):
        self.player_1,self.player_2 = self.set_players_position(player_1, player_2)
        """ while True:
            self.board,winner, tie = self.player_1.move(self.player_2, self.board)
            if winner or tie:
                return self.player_1.finish(winner,tie,self.board)
            self.board,winner, tie = self.player_2.move(self.player_1, self.board)
            if winner or tie:
                return self.player_2.finish(winner,tie,self.board) """
        input()
    
    def set_players_position(self, player_1, player_2):
        rand_pos = random.randint(1, 2)
        if rand_pos == 1:
            return player_1, player_2
        else:
            return player_2, player_1
    

    def mode_choise(self):
        self.wizard_talking(f"Hi, I am a {self.wizard_name}. The great wizard!")
        self.wizard_talking("Сhoose how you want to play")
        print("\n(1) - Human VS Human\n(2) - Human VS AI\n(3) - AI VS AI")
        user_input = ""
        while user_input != "1" and user_input != "2" and user_input != "3":
            user_input = self.check_input("\nCommand - ")
        return user_input

    def board_init(self):
        pass
