'''
Inheritance
from Textfile import CLASS

Called from (inheritanceChef.py)
'''
from chefClass import Chef
#inheritance from Class Chef
class AfricanChef(Chef):
    #overload function
    def make_special_dish(self):
        print("The chef makes rino stakes")

    def make_fried_planten(self):
        print("The chef makes fried planten ")