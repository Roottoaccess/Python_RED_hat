# Here we will learn to build about some scripts of building loops programs
# for i in range(1,11):
#     print(i)

# While loop script
# i = 1
# while(i < 51):
#     print(i)
#     i += 1

# i = 0
# while(i < 6):
#     print("python_snake")
#     i += 1

# List in loop
# l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

# i = 0
# while(i < len(l)):
#     print(l[i])
#     i += 1

# Foor loop scripting
# for i in range(4):
#     print(i)

# print("StepSizing in for loop")
# Step sizing
# for i in range(0, 10, 2):
#     print(i)

# print("List iteration using for loop")
# l1 = [1, 4, 6, 234, 6, 764]
# for i in l1:
#     print(i)

# print("This is a tupple iteration using for loop....")
# t = (6, 231, 75, 1220)

# for i in t:
#     print(i)

# print("String iteration")
# String iteration
# s = "Python_snake_hacking"
# for i in s:
#     print(i)

# For loop with else:....
# print("This is the else with for loop example....")
# ll = [1,8,88]

# for item in ll:
#     print(item)

# else:
#     print("done....") # this is printed when the loop exhausts!

# This is the break and continue statement in for loop

# Break statement
for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

# Continue statement
# Skip this iteration on continue
for i in range(100):
    if(i == 34):
        continue # It will only egnore the following condition and iterate the others
    print(i)

# Pass statement in for loop
# If we want to leave the for loop ideal and execute the while loop
# Then python has presented us with pass keyword very helpful
for i in range(645):
    pass

i = 0
while(i < 45):
    print(i)
    i += 1
