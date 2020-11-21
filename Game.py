from Global import *
from Inteligence import *

class Game(Global):
    
    player_1 = Inteligence
    player_2 = Inteligence

    def __init__(self):
        self.board_size = self.get_board_size_from_user()
    
    def game(self, player_1, player_2):
        self.player_1,self.player_2 = self.players_settings(player_1, player_2)
        while True:
            winner = self.player_1.move(self.player_2)
            if winner:
                return self.player_1.gratulation(self.player_2)
            winner = self.player_2.move(self.player_1)
            if winner:
                return self.player_2.gratulation(self.player_1)
        input()
    
    def players_settings(self, player_1, player_2):
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
                size = int(self.check_input("Size - "))
                if size > len(string.ascii_uppercase)-1:
                    self.wizard_talking("Size is too big, try smaller")
            except ValueError():
                self.wizard_talking("You shall not pass! Only digit :)")
        return size
    

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