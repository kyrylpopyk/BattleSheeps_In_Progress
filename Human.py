from Inteligence import *

class Human(Inteligence):

    def __init__(self, board_size):
        super().__init__(board_size)
        self.enemy_board = self.create_board([[]], board_size)
        self.board = self.create_board(self.board, board_size)
        self.registration_form()
        self.set_color()
        self.init_ships()
    
    def move(self, enemy):
        is_heated = True
        winner = False
        while is_heated:
            enemy_board = enemy.board
            self.clear_scr()
            self.print_board(enemy_board)
            self.print_both_board(enemy)
            row, col = self.get_fire_position()
            is_heated = self.fire(row, col, enemy)
            self.clear_scr()
            self.print_both_board(enemy)
            winner = self.is_winner()
            if winner:
                return winner
        return winner

    def get_fire_position(self):
        row = None
        col = ""

        print("Please input row and col then try to destroy enemy sheeps!")
        while col not in self.alfabet_list:
            col = self.check_input(f"Col(A-{self.alfabet_list[self.board_size - 1]}) -  ").upper()
            if col not in self.alfabet_list:
                print("Try again")
        col = self.alfabet_list.index(col)
        while row == None or row > len(self.board) or row < 0:
            try:
                row = int(self.check_input(f"Row(1-{len(self.board)}) - ")) - 1
            except ValueError:
                print("Try again")
        return row, col

    def registration_form(self):
        self.wizard_talking("Lets start the registration.")
        self.name = "Kyryll"#self.check_input("Please input Your name - ").capitalize() test
        self.clear_scr()
        self.wizard_talking("Nice to meet you " + self.name)
        self.wizard_talking("I suggest you choose your personal color")
    

    def set_color(self):
        self.print_colors(self.name)
        user_input = ""
        while user_input not in list(self.font_color.keys()):
            user_input = "Red"#self.check_input("Color name - ").capitalize() test
            try:
                self.color = self.font_color[user_input]
                self.b_color = self.background_color[user_input]
                self.name = self.color + self.name + Style.reset
                self.cell = self.b_color + "   " + Style.reset
                self.font_color.pop(user_input)
                return
            except KeyError:
                print("Only colors from the list!")
                continue

    def print_colors(self,text):
        print("\n /------------------\\")
        for index, value in self.font_color.items():
            print("|{:<18}-|-{:>18}|".format(value + index + self.reset, value + text + self.reset))
        print(" \------------------/\n")

    def init_ships(self):
        self.clear_scr()
        while self.is_ship_available():
            self.clear_scr()
            self.print_board(self.board)
            self.wizard_talking("Please input 'Ship name'/'Start position'/'Direction'.")
            print("Available ships:\n")
            for index,value in self.ship_size.items():
                print("({}) {:<11}{:>2}".format(self.ship_list.index(index) + 1,str(index)," - " + str(self.ship_count[index]) + "x"),end=" |")
                for i in range(value):
                    print(f"{self.cell}", end = "|")
                print("\n")
            ship_name = ""
            while ship_name not in list(self.ship_count.keys()):
                try:
                    ship_number = int(self.check_input(f"Ship(1-{len(self.ship_list)}) - ")) - 1 
                    ship_name = self.ship_list[ship_number]
                except Exception:
                    print("Try again")
                    continue
                if ship_name not in list(self.ship_count.keys()):
                    print("Incorect input!")
                    continue
                elif self.ship_count[ship_name] <= 0:
                    print("Select another shipt, this one is done")
                    ship_name = ""
                    continue
            col = " "
            while col not in string.ascii_uppercase:
                col = self.check_input(f"Col(A-{string.ascii_uppercase[len(self.board) - 1]}) -  ").upper()
            col = self.alfabet_list.index(col)
            row = None
            while row == None or row > len(self.board):
                try:
                    row = int(self.check_input(f"Row(1-{len(self.board)}) - ")) - 1
                except ValueError:
                    print("Only digit!")
            direction = self.get_direction()
            self.set_ship(row,col,ship_name,direction)
    
    def get_direction(self):
        direction = ""
        while direction not in self.ship_direction:
            direction = self.check_input("Direction(L/R/U/D) - ").upper()
        return direction
        


    
        
        
# 0. Создаем переменную is_destroy = false, запускаем цикл while is_destroy == False 
# 1.Мы наткнулись на хит: проверяем равняется ли имя данной переменной "Destroyer" если да  создаем переменную count = 1, записываем стартовые координаты start_row = 2, start_col = 5, проверяем все стороны, 