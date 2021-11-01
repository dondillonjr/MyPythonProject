#union Example

lettersA = {"a", "b", "c", "d"}
lettersB = {"a", "c", "e", "f"}

union = lettersA | lettersB
print("Union = ", union)
print(f"UNION = {union}")

intersection = lettersA & lettersB
print("Intersection = ", intersection)
print(f"INTERSECTION = {intersection}")

difference = lettersA - lettersB
print("Difference  = ", difference)
print(f"DIFFERENCE = {difference}")