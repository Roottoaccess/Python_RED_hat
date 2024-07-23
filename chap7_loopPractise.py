# This is the capter where we will practise loop scripting in python

# Question 1
# num = int(input("Enter any number: "))

# for i in range(1, 11):
#     res = num * i
#     print(num,"X",i,"=",res)

# Question 2
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if("S" in i):
#         print("Greetings for you",i)
# else:
#     print("Terminating the program....")

# Question 3
# num = int(input("Enter the number: "))
# i = 1

# while(i <= 10):
#     res = num * i
    # print(num,"X",i,"=",res)
    # print(f"{num} X {i} = {res}")
    # i += 1

# Question 4
# n = int(input("Enter number: "))

# for i in range(2, n):
#     if(n % i) == 0:
#         print("Number is not prime....")
#         break
# else:
#     print("Number is prime....")


# Question 5
# n = int(input("Enter the value of n: "))
# i = 1
# sum = 0
# while(i <= n):
#     sum += i
#     i += 1
# else:
#     print(f"The result is {sum}")

# Question 6
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1,num + 1):
#     fact *= i
# else:
#     print(f"The factorial {num} value is: {fact}")

# Question 7
'''
for n = 3
      *
     ***   
    *****
'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "*(n-i),end="")
    print("*"* (2*i-1), end = "")
    print("")

