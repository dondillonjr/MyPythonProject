'''
How to use imported modules
'''
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
musicGrates = ["James Brown", "Ray Charles", "Smokey Roberson", "Sam Cook"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

# roll num sided dice
def roll_dice(num):
    return random.randint(1, num)