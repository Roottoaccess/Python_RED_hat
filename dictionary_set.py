# This is a Dictionary and Set script in python

# Dictionary 
marks = {
    "harry": 100,
    "shubham": 56,
    "Rohan": 23,
    "list": [1,2,8]
}

# print(marks, type(marks))

# print(marks["harry"])

print(marks)

# Dictionary methods
print(marks.items())

print(marks.keys())

print(marks.values())

# Updating the dict
marks.update({"harry": 98, "Jeet": 100})
print(marks)

print(marks.get("Jeet")) # If the value is not present then it will give none
# but in the case of print(marks["Jeet"]) if the value is not present it will give an error that is not a good practise in python
# e = {} empty dictionary

# Sets - collection of well define objects
# s = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32 , 54 ,5, 5, 5, 5}
print(s, type(s))

# Sets methods

s1 = {"jeet", 1 ,2 , 3 , 4}
s1.add(588)
print(s1)

s1.remove(1)
print(s1)

# set union
s2 = {1, 45, 60, 78}
s4 = {14, 8, 1, 78}

print(s2.union(s4))

# set intersection
print(s2.intersection(s4))

