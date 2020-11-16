from Global import *
from Inteligence import *

class Game(Global):
    
    player_1 = Inteligence
    player_2 = Inteligence

    def __init__(self):
        self.make_dict_alfabet()
        self.board_size = self.get_board_size_from_user()
    
    def game(self, player_1, player_2):
        self.player_1,self.player_2 = self.players_settings(player_1, player_2)
        player_1.print_both_board(player_2)
        print(player_1.name)
        print(player_2.name)
        """ while True:
            winner, tie = self.player_1.move(self.player_2)
            if winner or tie:
                return self.player_1.finish(winner,tie,self.board)
            winner, tie = self.player_2.move(self.player_1)
            if winner or tie:
                return self.player_2.finish(winner,tie,self.board) """
        input()
    
    def players_settings(self, player_1, player_2):
        player_1, player_2 = self.game_ships_init(player_1,player_2) 
        rand_pos = random.randint(1, 2)
        if rand_pos == 1:
            return player_1, player_2
        else:
            return player_2, player_1
    
    def get_board_size_from_user(self):
        self.wizard_talking("Please input the size of the board. *Standart is 10x10 :) But not biggest then " + str(len(string.ascii_uppercase)) + "x" + str(len(string.ascii_uppercase)) + "!")
        size = None 
        while size == None:
            try:
                size = 10#int(self.check_input("Size - ")) test
                if size > len(string.ascii_uppercase)-1:
                    self.wizard_talking("Size is too big, try smaller")
            except ValueError():
                self.wizard_talking("You shall not pass! Only digit :)")
        return size

    def game_ships_init(self,player_1,player_2):
        player_1.init_ships()
        player_2.init_ships()
        return player_1, player_2
    

# Выбор вариации игры
# Создание таблицы
# Внесение информации о игроках(Выбор имени, выбор цвета, раставление кораблей)
# Ход игрока 1
# Проверка
# Ход игрока 2
# Проверка
# Повтор
# В случае выиграша или ничьи выводим комуникат в зависимости от того кто походил
# Повторить игру?