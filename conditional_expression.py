# This is the python script for conditional statement

# Age program
age = int(input("Enter your age: "))
if(age >= 18):
    # print("you are above the age of consent")
    # print("Good for you !")
    print("yes")
elif(age < 0):
    print("You are entering an invalid age")
elif(age == 0):
    print("You are entering 0 which is a valid age")
else:
    print("You are below the age of consent")

# if elif else ladder


print("End of the Program")