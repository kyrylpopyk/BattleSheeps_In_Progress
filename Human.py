from Inteligence import *

class Human(Inteligence):
    
    def __init__(self):
        self.name = self.regestration_form()

    def regestration_form(self):
        #time.sleep(0.5)
        self.wizard_talking("Lets start the registration.")
        #time.sleep(0.5)
        user_input = self.check_input("Please input Your name - ").capitalize()
        self.clear_scr()
        self.wizard_talking("Nice to meet you " + user_input)
        #time.sleep(0.5)
        self.wizard_talking("I suggest you choose your personal color")
        user_input = self.set_color(user_input)
        print(user_input)
        return user_input
    

    def set_color(self,value):
        self.print_colors(value)
        user_input = ""
        while user_input not in self.font_color.keys():
            user_input = self.check_input("Color name - ").capitalize()
        return self.font_color[user_input] + value + self.font_reset
        
