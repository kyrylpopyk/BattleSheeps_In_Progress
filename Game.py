from Global import *
from Inteligence import *

class Game(Global):

    def window(self):
        os.system('mode con: cols=100 lines=50')
    
    def game(self, player_1 = Inteligence,player_2 = Inteligence):
        """ self.player_1,self.player_2 = self.set_players_position(player_1, player_2)
        while True:
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