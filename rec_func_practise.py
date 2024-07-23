# This is the function and recursion practise questions solving

# Question 1

# Defining the function
# def NumMax():
#     num1 = int(input("Enter the number: "))
#     num2 = int(input("Enter the number: "))
#     num3 = int(input("Enter the number: "))

#     # Here goes the logic
#     if(num1 > num2 and num1 > num3):
#         return num1
#     elif(num2 > num1 and num2 > num3):
#         return num2
#     else:
#         return num3

# Calling the created function
# print(f"The maximum number is {NumMax()}")

# Question 2
# Converting Celsius to Fahrenheit program
# def conversion():
#     cel = int(input("Enter the Celsius: "))
#     # Now applying the logic

#     far = (cel * 1.8) + 32
#     return far

# Calling the function and displaying the result
# print(f"The fahrenheit for the following Celcius is: {conversion()}")

# Question 3
# How to prevent a print() function to print a ney line at the end
# print("Hello this is a python crash course", end = '')
# print(" hmmm.....")


# Question 4
# sum(n) = 1 + 2 + 3 + 4 .... n
# sum(n) = sum(n-1) + n
# def sum(n):
#     if(n == 1):
#         return 1
#     return sum(n - 1) + n

# Calling the function
# n = int(input("Enter the value of n: "))
# print(f"The result is: {sum(n)}")

# Question 5
# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n-1)
# pattern(5)

# Question 6
# def inch_converter(inch):

#     centimeter = inch * 2.54
#     return centimeter

# Calling the function
# inch = int(input("Enter the inch value: "))
# print(f"After converting to cm: {inch_converter(inch)}")

# Question 7
# l = ["Harry", "Rohan", "Shubham", "an"]
# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# print(rem(l, "an"))

# Question 8
# def table(num):
    
#     for i in range(1,11):
#         res = i * num
#         print(f"{num} X {i} = {res}")

# num = int(input("Enter value of num: "))
# table(num)