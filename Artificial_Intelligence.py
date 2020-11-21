from Inteligence import *

class Artificial_Intelligence(Inteligence):

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
            row, col = self.get_fire_position()
            is_heated = self.fire(row, col, enemy)
            winner = self.is_winner()
            if winner:
                return winner
        return winner
    
    def get_fire_position(self):
        row = None
        col = ""
        col = random.randint(0, self.board_size - 1)
        row = random.randint(0, self.board_size - 1)
        return row, col

    def registration_form(self):
        self.name = "Ork"
        self.set_random_color()
    
    def set_random_color(self):
        color_is_done = False
        while color_is_done != True:
            color_key = self.get_dict_key_name(self.font_color,random.randint(0,len(self.font_color)-1))
            self.color = self.font_color[color_key]
            self.b_color = self.background_color[color_key]
            self.cell = self.b_color + "   " + Style.reset
            self.name = self.color + self.name + Style.reset
            self.font_color.pop(color_key)
            color_is_done = True
        
    
    def init_ships(self):
        while self.is_ship_available():
            ship_name = self.get_ship()
            row = random.randint(0, len(self.board) - 1)
            col = random.randint(0, len(self.board) - 1)
            direction = self.ship_direction[random.randint(0, len(self.ship_direction) - 1)]
            self.set_ship(row, col, ship_name, direction)
            self.print_board(self.board)

    def get_ship(self):
        ship_is_done = False
        ship_name = ""
        while ship_is_done == False:
            ship_name = self.ship_list[random.randint(0,len(self.ship_list)-1)]
            if self.ship_count[ship_name] <= 0:
                continue
            else:
                ship_is_done = True
        return ship_name
    
    
