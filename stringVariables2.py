import keyword

name = 'dillon'

print(name)
print(name.upper())
print(name.replace('l','m'))

print(name == 'dillon')
print("don" != name)

print('house' in name)
print('dillon' not in name)

comment="Hello World" \
        "My name is "\
        "Don Dillon"
print(comment)

comment2="""
        Hello World
        My name is
        Don
        """
print(comment2)

hisName='Xavier'
email = """
        Hello {},
        How are you
        today?
        """
print(email.format(hisName))

hisName2='Etienne'
email = f"""
        Hello {hisName2}
        How are you today?
        Age {2 + 4}
        """
print(email)

print(keyword.kwlist)
#################
# Operator
print( 9 % 2)
print(10 / 2)
print(2 ** 2)

##Comparison Operator
print( 5 >= 3)
print( 5 == 3)
##logical operator
print( (5 > 4) and (3 > 1))
print((4 > 2) or (1 < 2))

##### if statements
num = -1
if num > 0:
        print(f"number {num} is positive")
elif num == 0:
        print(f"number {num} is zero")
else:
        print(f"number {num} is negative")

num2 = -1
if num2 > 0:
        print(f"number2 {num2} is positive")
else:
        print(f"number2 {num2} is zero negative")

num3 = 2
message = f"number3 [{num3}] is positive" if num3 > 0 else f"number3 [{num3}] is 0 or negative"
print(message)
