# This is the chapter 4 all about list in python
# Creating a list
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Roshan"]
# Printing the list
print(friends)

print(friends[0])

friends[0] = "Grapes"

print(friends)

# Unlike string lists are mutable, we can change it

print(friends[1: 4])

# List methods starting.....
# List are mutable
friends.append("Java")
print(friends)

# Sorting function in the list
l1 = [1, 34, 64 ,2, 6, 12]
# Sorting in asending order
l1.sort()
print(l1)

# Reverse function
l1.reverse()
print(l1)

# Insert function in list
l1.insert(3, 33333333)
print(l1)

# POP method in the list
l1.pop(3)
print(l1)

# Remove method in list
l1.remove(6)
print(l1)

# Tupples are immutable in python just like string
a = (1,2,3,4,5,False, "Rohan", "Shivamsukla")
print(type(a))
print(a)

# Tupple function in python.....
no = a.count(5)
print(no)

# Index function
ind = a.index("Rohan")
print(ind)

# Length of a
print(len(a))
