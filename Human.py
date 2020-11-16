from Inteligence import *

class Human(Inteligence):

    def __init__(self, board_size):
        super().__init__(board_size)
    
    def move(self, enemy):
        winner = False
        tie = True
        self.clear_scr()
        #row, col = get_fire_position()
        #enemy = fire(enemy, row, col)
        #winner, tie = fire_result(enemy)
        return enemy, winner, tie

    def get_fire_position(self):
        print("Please ")

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
                self.name = self.color + self.name + Style.font_reset
                self.cell = self.b_color + "   " + Style.Background_default
                self.font_color.pop(user_input)
                return
            except KeyError:
                print("Only colors from the list!")
                continue

    def print_colors(self,text):
        print("\n /------------------\\")
        for index, value in self.font_color.items():
            print("|{:<18}-|-{:>18}|".format(value + index + self.font_reset, value + text + self.font_reset))
        print(" \------------------/\n")

    def init_ships(self):
        self.clear_scr()
        while self.is_ship_available():
            self.clear_scr()
            self.print_board()
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
            col = self.alfabet_dict[col]
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
    
        
        
        
