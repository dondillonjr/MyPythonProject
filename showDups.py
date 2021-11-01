'''
Copy list (my_list) content to set (convert_set)

Afterwards, display items in list that are
repeated.  

Note: Dictionary not needed
USE: 5 lines of code
'''
my_list = [1,2,3,3,4,5,6,7,7,8,6,10,10,10,3,10]

#convert list to set (dups removed)
convert_set = set(my_list)

#traverse set - scan for set item in list
for num in convert_set:
    #show dups with repetitive count: (x > 1)
    if my_list.count(num) > 1:
        print(f"NUM:", num, "COUNT:", my_list.count(num))