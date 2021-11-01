'''
Go through list (my_list) and copy content to 
dictionary (my_dict)

Afterwards, display items in dictionary that are
repeated.  

Show the item repeated and its repetition count
'''
#my_list = [1,2,3,4,5,6,7,7,8,6,10]

my_list = [1,2,3,3,3,4,5,6,7,7,8,6,10,10,10,10]
#convert a list to a dictionary
#Dictionary comprehension use {}
my_dict = {}
defValue=1
for key in my_list:
    if ( key in my_dict ):
        bumpValue = my_dict[key]
        my_dict[key] = bumpValue + 1
    else:
        my_dict[key] = defValue

print(f"ORIG-LIST:", my_list)
print(f"Dictionary-Created:", my_dict)

#Show numbers in list that were repeated!
for key in my_dict:
    if my_dict[key] > 1:
        print(f"Num: {key}  Repeated: {my_dict[key]}")