### Class Attributes - attributes that are specific to the class
# not to an (instance or object) of that class

class Person:
    #number_of_people is attribute of class Person
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

#Note name will be different for each instance of class
#number_of_people will be the same value for each instance of class
p1 = Person("Tim")
print(p1.number_of_people)

p2 = Person("Jill")
print(p1.number_of_people)
