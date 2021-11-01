#### Phone Class

class Phone:
    def __init__(self, brand, price, color):
        ##Attributes
        self.brand = brand
        self.price = price
        self.color = color

    def make_call(self, phone_num):
        print(f"{self.brand} is calling {phone_num}")

    def __str__(self) -> str:
        #return super().__str__()
        return f"BRAND = {self.brand}  \nPRICE={self.price} \nCOLOR={self.color}"

########### Create Phones

iphone  = Phone("Apple I7", 300, "black")
samsung = Phone("Samsung Gx20", 400, "Silver")

print(iphone.price)
print(iphone.brand)
print(iphone.color)

print()
print(samsung.price)
print(samsung.brand)
print(samsung.color)
print()
iphone.make_call(7779311)
print()
#note toString Python method has been overwitten
print(iphone)
print()
print(samsung)