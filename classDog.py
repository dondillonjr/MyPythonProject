## Example of Dog Class

class Dog:
    def __init__(self, name, age, location):
        self.name = name
        self.age  = age
        self.location = location

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_location(self):
        return self.location

    def set_age(self, age):
        self.age = age

    def set_location(self, location):
        self.location = location


dogs = []
myDog   = Dog("Raph", 4, "Georgia")
myDog2  = Dog("Tommas", 6, "Forida")
print(f"{myDog.get_name()}  {myDog.get_age()} {myDog.get_location()}")
print(f"{myDog2.get_name()}  {myDog2.get_age()} {myDog2.get_location()}")
myDog.set_age(6)
print(f"{myDog.get_name()}  {myDog.get_age()} {myDog.get_location()}")
