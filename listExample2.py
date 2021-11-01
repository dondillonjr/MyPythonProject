#LIST Example

my_list  = [1, 2, 3, 4, 5, 0, -1, ['A', "Don", 50]]
my_list2 = [1, 2, 3, 4, 5, 0, -1]
print(my_list)
print(my_list[6])
print(my_list[7][0])
print(my_list[7][1])
print(my_list[7][2])

my_list2.sort()
print(my_list2)

my_list2.reverse()
print(my_list2)

print(len(my_list))
print(len(my_list2))

my_list2.append(100)
print(len(my_list2))
print(my_list2)

store_b = 5 in my_list2
print("Check if 5 in list = ", store_b)

my_list2.remove(-1)
print(my_list2)

my_list2.pop()
print(my_list2)

del my_list2[2]
print(my_list2)

del my_list2[1:3]
print(my_list2)

my_list2.clear()
print("After Clear", my_list2)