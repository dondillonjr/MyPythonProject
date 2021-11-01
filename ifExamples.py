# if statements

is_male = False
is_tall = False


def determineMale(male, tall):
    if male and tall:
        print("You are a tall male")
    elif male and not tall:
        print("You are a short male")
    elif not male and tall:
        print("Your are a tall female")
    else:
        print("You are a short female")

### determine largest number
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
###################### MAIN ##############
determineMale(is_male,is_tall)
#print(max_num(0 , 20, 3))