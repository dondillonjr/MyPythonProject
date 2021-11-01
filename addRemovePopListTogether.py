numbers = [ 1, 2, 3, 4, 5 ]

characters = [ "abc", "def", "ghi"]

#add list together
numbers.extend(characters)
print(numbers)

#add item to end of list
numbers.append("XYZ")
print(numbers)

#add item to a specific location
numbers.insert(2, "2.5")
print(numbers)

#remove item from a list
numbers.remove("XYZ")
print(numbers)
numbers.remove("2.5")
print(numbers)

#clear list
numbers.clear()
print(numbers)

#remove last element in list
characters.pop()
print(characters)

#check to see if def is in list
print(characters.index("def"))

#add item to end of list
characters.append("abc")
print(characters)

#count number of occurances of "abc"
print(characters.count("abc"))
print(characters)

#sort list fields
characters.sort()
print(characters)

#reverse list items
characters.reverse()
print(characters)

friends = characters.copy()
print(friends)
