# Create Student Class
# Called by (student.py)
class Student:
    #define student attributes
    def __init__(self, name, major, gpa, address, deans_list):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.address = address
        self.deansList = deans_list

    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False