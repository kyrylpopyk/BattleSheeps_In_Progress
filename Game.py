from Global import *
from Inteligence import *

class Game(Global):
    
    player_1 = Inteligence()
    player_2 = Inteligence()

    def window(self):
        os.system('mode con: cols=100 lines=25')
    
    def game(self, player_1, player_2):
        self.player_1,self.player_2 = self.players_settings(player_1, player_2)
        """ while True:
            self.board,winner, tie = self.player_1.move(self.player_2, self.board)
            if winner or tie:
                return self.player_1.finish(winner,tie,self.board)
            self.board,winner, tie = self.player_2.move(self.player_1, self.board)
            if winner or tie:
                return self.player_2.finish(winner,tie,self.board) """
        input()
    
    def players_settings(self, player_1, player_2):
        player_1, player_2 = self.board_init(player_1, player_2)
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

    def board_init(self,player_1, player_2):
        self.wizard_talking("Please input the size of the board. *Standart is 10 :) But not biggest then " + str(len(string.ascii_uppercase)))
        size = 20#None test
        while size == None:
            try:
                size = int(self.check_input("Size - "))
                if size > len(string.ascii_uppercase)-1:
                    self.wizard_talking("Size is too big, try smaller")
            except ValueError():
                self.wizard_talking("You shall not pass! Only digit :)")

        for i in range(size):
            for j in range(size):
                player_1.board[i].append(Inteligence().empty_cell)
            if i == size - 1:
                break
            player_1.board.append([])
        
        for i in range(size):
            for j in range(size):
                player_2.board[i].append(Inteligence().empty_cell)
            if i == size - 1:
                break
            player_2.board.append([])
        player_1 = self.init_sheeps(player_1)
        return player_1, player_2
    

    def init_sheeps(self,player = Inteligence):
        while True:
            player.print_board()
            self.wizard_talking("Please select the position when you want to put your speep")
            row = int(self.check_input("Row - "))
            col = int(self.check_input("Col - "))
            player.board[row][col] = player.sheep
            self.clear_scr()
        input()
        return player
        


