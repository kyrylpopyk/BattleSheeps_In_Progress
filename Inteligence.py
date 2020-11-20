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
        self.ship_count = {"Cruiser":1,"Battleship":1}#{"Destroyer":4,"Submarine":3,"Cruiser":2,"Battleship":1} test
        self.ship_size = {"Cruiser":3,"Battleship":4}#{"Destroyer":1,"Submarine":2,"Cruiser":3,"Battleship":4} test
        self.ship_list = ["Cruiser","Battleship"]#["Destroyer","Submarine","Cruiser","Battleship"] test
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
    
    def print_both_board(self,enemy):
        size = len(self.board)
        print("   {:^50}{}{:^50}".format(self.name," " * 13, enemy.name))
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
                print(self.enemy_board[row][col].cell, end="|")
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
            self.board[row-1][col].cell_status = False
        if row - 1 >= 0 and col + 1 <= len(self.board)-1:                   #Up-Right
            self.board[row-1][col+1].cell_status = False
        if row - 1 >= 0 and col - 1 >= 0:                                   #Up-Left
            self.board[row-1][col-1].cell_status = False
        if row + 1 <= len(self.board)-1:                                    #Down
            self.board[row+1][col].cell_status = False           
        if row + 1 <= len(self.board)-1 and col + 1 <= len(self.board)-1:   #Down-Right
            self.board[row+1][col+1].cell_status = False
        if row + 1 <= len(self.board)-1 and col - 1 >= 0:                   #Down-Left
            self.board[row+1][col-1].cell_status = False
        if col + 1 <= len(self.board)-1:                                    #Right
            self.board[row][col+1].cell_status = False
        if col - 1 >= 0:                                                    #Left
            self.board[row][col-1].cell_status = False
    

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
        self.print_both_board(enemy)
        print(f"{self.name} is winner!!! Congratulation!!!")
        input()

        
    