from Inteligence import *

class Human(Inteligence):
    board = [[]]

    def __init__(self):
        self.name = self.registration_form()

    def registration_form(self):
        self.wizard_talking("Lets start the registration.")
        user_input = "Kyryll"#self.check_input("Please input Your name - ").capitalize() test
        self.clear_scr()
        self.wizard_talking("Nice to meet you " + user_input)
        self.wizard_talking("I suggest you choose your personal color")
        user_input = self.set_color(user_input)
        print(user_input)
        return user_input
    

    def set_color(self,value):
        self.print_colors(value)
        user_input = ""
        while user_input not in self.font_color.keys():
            user_input = "Red"#self.check_input("Color name - ").capitalize() test
            self.sheep = Style.Background_lightRed + "   " + Style.Background_default
        return self.font_color[user_input] + value + self.font_reset
        
    
    def move(self,enemy):
        pass
