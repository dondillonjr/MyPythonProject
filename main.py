# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import importFiles

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi " + name)  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(25)
print(3 * 2)
print("1 + 2 = ", 1 + 2)
print("Hello", "World" , sep="---")
print("Hello", " ", "World")
x=10
y=20.5678
name="Don"
print("NAME %s" % name)
print("Name= %s Number= %d FLOAT= %.2f" % (name, x, y))
print("(0) * (1) = (5)".format(x, y, x * y))

value = int (input("Enter a number: "))
print( value + 6)
print("\n")
print(importFiles.roll_dice(10))
print(importFiles.musicGrates)

#####################
myName='DILLON'
newAge=20
PI=3.14
myNumbers=[1,2,3,4]
middleName, addressNumber = "Bolden", 340
oldNumber=[]
isAdult=True
print(type(myNumbers))
print(type(newAge))
print(type(oldNumber))
print(type(isAdult))
print(type(myName))
print(type(addressNumber))
print(type(PI))
print(myNumbers)