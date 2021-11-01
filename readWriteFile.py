'''
Reading from a file
'''


#OPEN TEXT FILE for read and write
employee_file = open("employee.txt", "r+")

if employee_file.readable() == True:
    #read all file content
    print(employee_file.read())
employee_file.close()

print("two\n")
employee_file = open("employee.txt", "r+")
print(employee_file.readlines()[1])
employee_file.close()

print("three\n")
employee_file = open("employee.txt", "r+")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

print("four\n")
#append to end of file
employee_file = open("employee.txt", "a")
employee_file.write("\nBarbara Dillon Professional Teacher")
employee_file.close()

print("five\n")
#create new file
employee_file = open("employee2.txt", "w")
employee_file.write("Barbara Dillon Professional Teacher")
employee_file.close()

print("six\n")
#over-write file
employee_file = open("employee2.txt", "w")
employee_file.write("Don Dillon Professional Software Developer")
employee_file.close()