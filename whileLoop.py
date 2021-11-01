#While LOOP

a = 1
while a <= 3:
    print(a)
    a += 1;


guess = ""
i=0
limit=5
secret_word = "stop"
while guess != secret_word and i < limit:
    if i < limit:
        guess = input("Enter guess:")
        i += 1

if i == limit:
    print("you lose")
else:
    print ("You Win")