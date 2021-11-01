## check if file exist before attempting to read from it

import os.path

filename = "c:/temp/test.txt"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")