'''
from file (studentClass.py) import class (Student)
Calls class Student in (studentClass.py)
'''
from studentClass import Student
student1 = Student("Don", "Engineering", 1.2, "Atlanta Ga", True)
student2 = Student("Pam", "Art", 4.0, "Atlanta Ga", True)

print(student1.name)
#print(student1.major)
print(student1.gpa)
print(student1.honor_roll())
print("\n")
print(student2.name)
#print(student2.major)
print(student2.gpa)
print(student2.honor_roll())
