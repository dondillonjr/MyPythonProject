### Writing to a file

my_file = open("c:/temp/test.txt", "w")

my_file.write("ID, Name, Email\n")
my_file.write("1, Don, don@com\n")
my_file.write("2, Xavier, xavier@com\n")
my_file.write("3, Etienne, etienne@com\n")
my_file.close

my_file = open("c:/temp/test.txt", "r")
print(my_file.read())
my_file.close()
print()
print()

my_file = open("c:/temp/test.txt", "a")
my_file.write("4, Rhonda, rhonda@com\n")
my_file.close()

my_file = open("c:/temp/test.txt", "r")
for line in my_file:
    print(line)
my_file.close()
print()
print()
my_file = open("c:/temp/test.txt", "r")
print(my_file.readlines())
my_file.close()

