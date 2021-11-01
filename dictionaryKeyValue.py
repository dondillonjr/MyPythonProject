## dictionary - name - value pair data structure

person = {   #key    #value
            "name":    "Don",
            "age":     50,
            "address": "USA"
}

print(person)
print(person["age"])
print(person.keys())
print(person.values())

print(person.get("age"))
person["age"] = 60
print(person)

############################
mynames ={"Dillon", "Eliotte", "Lee"}
names=["Don","Xavier","Etienne"]

for name in names:
    print(name)

for name in mynames:
    print(name)

##########################
for key in person:
    print(f"Key: {key}  Value: {person[key]}")
print()
print(person.items())
print()

for key, value in person.items():
    print(f"KEY: {key}  VALUE: {value}")
