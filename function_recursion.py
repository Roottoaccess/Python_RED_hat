# This is the function_and_recurtion scripting concept in python

# Creating the function
# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))

#     avg = (a + b + c) / 3
#     print(avg)

# Calling the function
# avg() # Running the function


# Quick question on function

# Creating the function defination
# def username():
#     name = input("Enter your name please: ")
#     print(f"Hello and welcome to our hotel MR {name}")

# Calling the function
# username()

# Another way to solve this script
# def goodDay(name):
#     print("Good Day, "+ name)

# goodDay("python_snake")

# Default parameter concept in python....
# def goodDay(name, ending = "Bot"):
#     print(f"Good Day, {name}")
#     print(ending)

# goodDay("Python", "Robot")


# Recursion concept in python
'''
    factorial(5) = 5 * 4 * 3 * 2 * 1 
    factorial(n) = n * factorial(n - 1)
'''

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of the number is: {factorial(n)}")