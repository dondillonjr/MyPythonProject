## Example of Inheritance in Python
####################################
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name}. I am {self.age} years old")

    def speak(self):
        print("I don't know how to speak")

####################################
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")

    def show(self):
        print(f"My name is {self.name}. I am {self.age} years old. My color is {self.color}")

####################################
class Dog(Pet):
    def speak(self):
        print("Woof")
###################################
pet = Pet("Shaft", 1)
pet.show()
pet.speak()
print()
cat = Cat("MeMe", 4, "Gold")
cat.show()
cat.speak()
print()
dog = Dog("Major", 3)
dog.show()
dog.speak()
pet.speak()