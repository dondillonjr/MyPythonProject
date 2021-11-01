'''
Inheritance
from file import ClASS

Calls class (Chef) in file chefClass.py
Calls class (AfricanChef) in file africanChefClass.py
'''
from chefClass import Chef
from africanChefClass import AfricanChef

myChef = Chef()
myChef.make_checken()
myChef.make_special_dish()
print("\n")
myAfricanChef = AfricanChef()
myAfricanChef.make_checken()
myAfricanChef.make_fried_planten()
myAfricanChef.make_special_dish()