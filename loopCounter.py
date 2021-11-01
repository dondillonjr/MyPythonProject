numbers = [1, 2, 3, 4, 5]
result  = 0

for num in numbers:
    #result = result + num
    result += num
print("SUM Total=", result)

for n in [1, 2, 3, 4, 5]:
    print(n)

print()

num=0
while num < 20:
    num += 1

    if (num == 19):
        print("I hit 19")
        break

    #show only even numbers
    if (num % 2 == 0):
        print(num)
    else:
        continue
else:
    print("loop Terminated")