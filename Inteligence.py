from Global import *


class Inteligence(Global):
    
    name = ""
    color = ""
    empty_cell = Style.Background_lightBlue + "   " + Style.Background_default
    miss_cell = Style.Background_default + " M " + Style.Background_default
    sheep = color + "   " + Style.Background_default

    def print_board(self):
        size = len(self.board)
        print("     ", end= "")
        for i in range(size):
            print(string.ascii_uppercase[i], end="   ")
        print()
        for row in range(size):
            print("{:<2} |".format(str(row + 1)), end = "")
            for col in range(size):
                print(self.board[row][col], end="|")
            print("")
            print("   " + "----" * size + "-")
        
    