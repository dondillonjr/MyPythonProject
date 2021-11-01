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

    def speak(self) -> str:
        return "Woff Woff\n"

dogs = []
dogs.append(Dog("Raph", 4, "Georgia"))
dogs.append(Dog("Tommas", 6, "Forida"))
dogs.append(Dog("Major", 3, "Baton"))
dogs.append(Dog("Sheba", 2, "Atlanta"))


for dog in dogs:
    #print(dog)
    print( dog.name , dog.age, dog.location, dog.speak())

