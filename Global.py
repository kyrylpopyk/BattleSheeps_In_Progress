import os
import sys
import random
import time
import string

class Global(object):
    wizard_name = "Gandalf"
    font_color = {"Red":"\033[91m","Green":"\033[92m","Yellow":"\033[93m","Blue":"\033[94m","Purple":"\033[95m","Cyan":"\033[96m","White":"\033[97m"}
    font_reset = "\u001b[0m"

    def print_colors(self,text):
        print("\n /------------------\\")
        for index, value in self.font_color.items():
            print("|{:<18}-|-{:>18}|".format(value + index + self.font_reset, value + text + self.font_reset))
        print(" \------------------/\n")
    
    def check_input(self, text):
        user_input = input(text)
        if user_input == "quit":
            quit()
        elif user_input == "restart":
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            return user_input
    
    def clear_scr(self):
        os.system("cls || clear")

    def wizard_talking(self,text):
        print(self.wizard_name + ": " + text)

class Style():
    font_purple = '\033[95m'
    font_blue = '\033[94m'
    font_cyan = '\033[96m'
    font_green = '\033[92m'
    font_yellow = '\033[93m'
    font_red = '\033[91m'
    font_white = '\033[0m'
    font_bold = '\033[1m'
    font_reset = '\u001b[0m'
    font_underline = '\033[4m'

