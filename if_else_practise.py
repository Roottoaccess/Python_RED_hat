# This is the practise script in python for conditional statement


# Question 1
# num = int(input("Enter number: "))
# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))
# num3 = int(input("Enter number: "))

# if(num > num1 and num > num2 and num > num3):
#     print("The greatest number is:",num)
# elif(num1 > num and num1 > num2 and num1 > num3):
#     print("The greatest number is:",num1)
# elif(num2 > num and num2 > num1 and num2 > num3):
#     print("The greatest number is:",num2)
# else:
#     print("The greatest number is:",num3)
# print("Program Ended !")

# Question 2
# maths = int(input("Enter the marks of maths:  "))
# eng = int(input("Enter the marks of english: "))
# science = int(input("Enter the marks of science: "))

# Check for total percentage
# per = int((maths + eng + science) / 3)
# print(int(per))

# if(per >= 40 and maths > 33 and eng > 33 and science > 33):
#     print("you are pass",per)
# else:
#     print("not pass but dont lose hope try again you will surely get it",per)

# Question 3
# Spam msg detection
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# msg = input("Enter your comment: ")

# if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
#     print("This is a spam message !")
# else:
#     print("This is a normal message !")

# Question 4
# Write a python script to find whether a given username contains less than 10 characters or not

# username = input("Enter your username: ")

# count = len(username)

# Appling the logic
# if(count < 10):
#     print("Username contains less than 10 characters..")
# else:
#     print("Username contains more than 10 characters..")


# Question 5
# l = ["Harry", "Rohan", "Shubham", "Divya"]

# name = input("Enter the name: ")

# if(name in l):
#     print("This name is present in the list")
# else:
#     print("This name is not present in the list..")

# Question 6
# Grade calculate script

# marks = int(input("Enter the marks: "))

# if(marks >= 90 and marks < 100):
#     print("Ex")
# elif(marks >= 80 and marks < 90):
#     print("A")
# elif(marks >= 70 and marks < 80):
#     print("B")
# elif(marks >= 60 and marks < 70):
#     print("C")
# elif(marks >= 50 and marks < 60):
#     print("D")
# else:
#     print("F")

# Question 7
post = input("Enter the post: ")

if("harry" in post.lower()):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry..")
