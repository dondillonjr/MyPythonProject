'''
Examples of try/catch blocks
'''

try:
    value = 10 / 0
    number = int(input("Enter a float number: "))
    print(number)
except ValueError as err:
    print("invalid Input")
    print(err)
except ZeroDivisionError as err:
    print(err)
