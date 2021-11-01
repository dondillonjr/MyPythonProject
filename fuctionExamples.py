#def = fuction

def my_fuction(name, age):
    print("Hello " + name)
    print("You are " + str(age))

def cube(num):
    return num * num * num

#set a default for age to (-1)
def greet(myname, myage=-1):
    print(f"Hello {myname}")
    if myage >= 0:
        print(f"Your age is {myage}")

def is_adult(age):
    if age >= 16:
        print("adult :)")
    else:
        print("not yet an adult  :(")

def is_adult2(age):
    return age >= 16

def get_Gender(gender="unknow"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"gender {gender} is unknown"

################# MAIN #################
print("Top")
#call function
my_fuction("DON", 30)
result = cube(3)
print(result)
print("Bottom")
print()
greet("DONNIE", 30)
is_adult(22)
is_adult(10)
print()
result = is_adult2(30)
print(f"Are you an Adult: {result}")

result = is_adult2(12)
print(f"Are you an Adult: {result}")
print()
print(get_Gender("f"))
print(get_Gender("m"))
print(get_Gender("Man"))