#translate
'''
   Single Quotes make multi line comments
   test
'''

def translate(phase):
    translation = ""

    for letter in phase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

################## Main ###############
''' comments
user data:
dog
house
'''

print(translate(input("Enter a phase: ")))