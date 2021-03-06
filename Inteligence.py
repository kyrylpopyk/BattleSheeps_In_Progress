from Global import *

class Inteligence(Global):
    def __init__(self, board_size = 0):
        self.board = [[]]
        self.board_size = board_size
        self.cell_ship_name = ""
        self.ship_coordinates = []
        self.name = ""
        self.color = ""
        self.b_color = "\033[104m"
        self.global_ship_count_cell = 0
        self.alfabet_list = []
        self.make_dict_alfabet(self.board_size)
        self.cell_status = True
        self.cell = Style.Background_lightBlue + "   " + Style.reset
        self.miss_cell = Style.reset + " M " + Style.reset
        self.ship_count = {"Destroyer":4,"Submarine":3,"Cruiser":2,"Battleship":1}
        self.ship_size = {"Destroyer":1,"Submarine":2,"Cruiser":3,"Battleship":4}
        self.ship_list = ["Destroyer","Submarine","Cruiser","Battleship"]
        self.enemy_board = []
    
    def make_dict_alfabet(self, size):
        for index in range(size):
            self.alfabet_list.append(string.ascii_uppercase[index])
    
    def init_ships(self):
        pass

    def set_color(self):
        pass

    def registration_form(self):
        pass
    
    def create_board(self, board, board_size):
        for i in range(board_size):
            for j in range(board_size):
                board[i].append(Inteligence())
            if i == board_size - 1:
                break
            board.append([])
        return board

    def print_board(self, board):
        size = len(board)
        print("     ", end= "")
        for i in range(size):
            print(string.ascii_uppercase[i], end="   ")
        print()
        for row in range(size):
            print("{:<2} |".format(str(row + 1)), end = "")
            for col in range(size):
                print(board[row][col].cell, end="|")
            print("")
            print("   " + "----" * size + "-")
    
    def print_both_board(self, second_board, enemy_name):
        size = len(self.board)
        print("   {:^50}{}{:^50}".format(self.name," " * 13, enemy_name))
        print("     ", end= "")
        for i in range(size):                               #1
            print(string.ascii_uppercase[i], end="   ")
        print("              ", end = "")
        for i in range(size):                               #2
            print(string.ascii_uppercase[i], end="   ")
        print()
        for row in range(size):
            print("{:<2} |".format(str(row + 1)), end = "") #1
            for col in range(size):
                print(self.board[row][col].cell, end="|")
            print("          ", end = "")
            print("{:<2} |".format(str(row + 1)), end = "") #2
            for col in range(size):
                print(second_board[row][col].cell, end="|")
            print()
            print("   " + "----" * size + "-" + "             " + "----" * size + "-")
    
    def get_ship_coordinate(self, row, col, ship_name, direction):
        coordinate_llist = []
        if direction == "L":
            for i in range(self.ship_size[ship_name]):
                coordinate_llist.append([row,col])
                col -= 1
        elif direction == "R":
            for i in range(self.ship_size[ship_name]):
                coordinate_llist.append([row,col])
                col += 1
        elif direction == "D":
            for i in range(self.ship_size[ship_name]):
                coordinate_llist.append([row,col])
                row += 1
        elif direction == "U":
            for i in range(self.ship_size[ship_name]):
                coordinate_llist.append([row,col])
                row -= 1
        return coordinate_llist
        
    
    def set_ship(self,row,col,ship_name,direction):
        if direction == "L":
            if self.is_able_to_put_sheep(row,col,ship_name,direction):
                ship_coordinates = self.get_ship_coordinate(row,col,ship_name,direction)
                for index in range(self.ship_size[ship_name]):
                    self.board[row][col] = copy(self)
                    self.board[row][col].ship_coordinates = ship_coordinates
                    self.change_cell_status_around(row,col)
                    self.board[row][col].cell_ship_name = ship_name
                    self.global_ship_count_cell += 1
                    col -= 1
                self.ship_count[ship_name] -= 1
            else:
                print("This place is not available to put the ship")
        elif direction == "R":
            if self.is_able_to_put_sheep(row,col,ship_name,direction):
                ship_coordinates = self.get_ship_coordinate(row,col,ship_name,direction)
                for index in range(self.ship_size[ship_name]):
                    self.board[row][col] = copy(self)
                    self.board[row][col].ship_coordinates = ship_coordinates
                    self.change_cell_status_around(row,col)
                    self.board[row][col].cell_ship_name = ship_name
                    self.global_ship_count_cell += 1
                    col += 1
                self.ship_count[ship_name] -= 1
            else:
                return False
        elif direction == "U":
            if self.is_able_to_put_sheep(row,col,ship_name,direction):
                ship_coordinates = self.get_ship_coordinate(row,col,ship_name,direction)
                for index in range(self.ship_size[ship_name]):
                    self.board[row][col] = copy(self)
                    self.board[row][col].ship_coordinates = ship_coordinates
                    self.change_cell_status_around(row,col)
                    self.board[row][col].cell_ship_name = ship_name
                    self.global_ship_count_cell += 1
                    row -= 1
                self.ship_count[ship_name] -= 1
        elif direction == "D":
            if self.is_able_to_put_sheep(row,col,ship_name,direction):
                ship_coordinates = self.get_ship_coordinate(row,col,ship_name,direction)
                for index in range(self.ship_size[ship_name]):
                    self.board[row][col] = copy(self)
                    self.board[row][col].ship_coordinates = ship_coordinates
                    self.change_cell_status_around(row,col)
                    self.board[row][col].cell_ship_name = ship_name
                    self.global_ship_count_cell += 1
                    row += 1
                self.ship_count[ship_name] -= 1
    
    def change_cell_status_around(self,row,col):
        self.board[row][col].cell_status = False                            #Middle
        if row - 1 >= 0:                                                    #Up
            self.change_color_status_around(row - 1, col)
        if row - 1 >= 0 and col + 1 <= len(self.board)-1:                   #Up-Right
            self.change_color_status_around(row - 1, col + 1)
        if row - 1 >= 0 and col - 1 >= 0:                                   #Up-Left
            self.change_color_status_around(row - 1, col - 1)
        if row + 1 <= len(self.board)-1:                                    #Down
            self.change_color_status_around(row + 1, col)       
        if row + 1 <= len(self.board)-1 and col + 1 <= len(self.board)-1:   #Down-Right
            self.change_color_status_around(row + 1, col + 1)
        if row + 1 <= len(self.board)-1 and col - 1 >= 0:                   #Down-Left
            self.change_color_status_around(row + 1, col - 1)
        if col + 1 <= len(self.board)-1:                                    #Right
            self.change_color_status_around(row, col + 1)
        if col - 1 >= 0:                                                    #Left
            self.change_color_status_around(row, col - 1)
    
    def change_color_status_around(self, row, col):
        self.board[row][col].cell_status = False

    

    def is_able_to_put_sheep(self, row, col, ship_name, direction):
        if direction == "L":
            if col - self.ship_size[ship_name] + 1 < 0:
                return False
            for element in range(self.ship_size[ship_name]):
                if self.board[row][col].cell_status == False:
                    return False
                col -= 1
        elif direction == "R":
            if col + self.ship_size[ship_name]> len(self.board):
                return False
            for element in range(self.ship_size[ship_name]):
                if self.board[row][col].cell_status == False:
                    return False
                col += 1
        elif direction == "U":
            if row - self.ship_size[ship_name] + 1 < 0:
                return False
            for element in range(self.ship_size[ship_name]):
                if self.board[row][col].cell_status == False:
                    return False
                row -= 1
        elif direction == "D":
            if row + self.ship_size[ship_name] > len(self.board):
                return False
            for element in range(self.ship_size[ship_name]):
                if self.board[row][col].cell_status == False:
                    return False
                row += 1
        return True

    def is_ship_available(self):
        summ = 0
        for i in self.ship_count.values():
            summ += i
        if summ == 0:
            return False
        else:
            return True
    

    def is_winner(self):
        if self.global_ship_count_cell == 0:
            return True
        else:
            return False

    def gratulation(self, enemy):
        self.clear_scr()
        self.print_both_board(enemy.board, enemy.name)
        print(f"{self.name} is winner!!! Congratulation!!!")
        input()
    
    def fire(self, row, col, enemy):
        if enemy.board[row][col].cell == self.change_cell_symbole(Style.font_black + "H", enemy):
            print()
        if enemy.board[row][col].cell == enemy.cell:
            self.enemy_board[row][col].cell = self.change_cell_symbole(Style.font_black + "H", enemy)
            enemy.board[row][col].cell = self.change_cell_symbole(Style.font_black + "H", enemy)
            self.destroying(row, col, enemy)
            self.global_ship_count_cell -= 1
            return True
        elif enemy.board[row][col].cell != self.change_cell_symbole(Style.font_black + "H", enemy):
            enemy.board[row][col].cell = self.change_cell_symbole(Style.font_black + "M", Inteligence())
            self.enemy_board[row][col].cell = self.change_cell_symbole(Style.font_black + "M", Inteligence())
            return False
    
    def change_cell_symbole(self, symbole_change, player):
        return player.b_color + f" {symbole_change} " + Style.reset
    
    def destroying(self, row, col, enemy):
        hit_count = 0
        test1 = enemy.board[row][col].cell_ship_name
        for i in range(self.ship_size[enemy.board[row][col].cell_ship_name]):
           coordinate_row = enemy.board[row][col].ship_coordinates[i][0]
           coordinate_col = enemy.board[row][col].ship_coordinates[i][1]
           if enemy.board[coordinate_row][coordinate_col].cell == enemy.board[row][col].cell:
               hit_count += 1
        if hit_count == self.ship_size[enemy.board[row][col].cell_ship_name]:
            for i in range(self.ship_size[enemy.board[row][col].cell_ship_name]):
                coordinate_row = enemy.board[row][col].ship_coordinates[i][0]
                coordinate_col = enemy.board[row][col].ship_coordinates[i][1]
                enemy.board[coordinate_row][coordinate_col].cell = self.change_cell_symbole(Style.font_black + "D", enemy)
                self.enemy_board[coordinate_row][coordinate_col].cell = self.change_cell_symbole(Style.font_black + "D", enemy)

    def get_fire_position(self):
        pass

        
    