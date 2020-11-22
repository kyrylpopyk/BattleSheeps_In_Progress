import os
import sys
import random
import time
import string
from copy import copy

class Global(object):
    wizard_name = "Gandalf"
    font_color = {"Red":"\033[91m","Green":"\033[92m","Yellow":"\033[93m","Purple":"\033[95m"}
    background_color = {"Red":"\033[41m","Green":"\033[42m","Yellow":"\033[43m","Purple":"\033[45m"}
    ship_direction = ["R","L","U","D"]
    reset = "\u001b[0m"
    def check_input(self, text):
        user_input = input(text)
        if user_input.lower() == "quit":
            quit()
        elif user_input.lower() == "restart":
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            return user_input
    
    def clear_scr(self):
        os.system("cls || clear")

    def wizard_talking(self,text):
        print(self.wizard_name + ": " + text)
    
    def get_dict_key_name(self,dictionary = dict,int_key = None):
        i = 0
        for key in dictionary.keys():
            if i == int_key:
                return key
            else:
                i += 1

class Style():
    font_black = '\033[30m'
    font_purple = '\033[95m'
    font_blue = '\033[94m'
    font_cyan = '\033[96m'
    font_green = '\033[92m'
    font_yellow = '\033[93m'
    font_red = '\033[91m'
    font_white = '\033[0m'
    font_bold = '\033[1m'
    reset = '\u001b[0m'
    font_underline = '\033[4m'
    Background_black        = "\033[40m"
    Background_red          = "\033[41m"
    Background_green        = "\033[42m"
    Background_yellow       = "\033[43m"
    Background_blue         = "\033[44m"
    Background_magenta      = "\033[45m"
    Background_cyan         = "\033[46m"
    Background_lightGray    = "\033[47m"
    Background_darkGray     = "\033[100m"
    Background_lightRed     = "\033[101m"
    Background_lightGreen   = "\033[102m"
    Background_lightYellow  = "\033[103m"
    Background_lightBlue    = "\033[104m"
    Background_lightMagenta = "\033[105m"
    Background_lightCyan    = "\033[106m"
    Background_white        = "\033[107m"