# This is the project 1 script for making a game
import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("Game draw")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you Lose !")
    elif(computer == 1 and you == -1):
        print("you lose !")
    elif(computer == 1 and you == 0):
        print("you win !")
    elif(computer == 0 and you == -1):
        print("you lose !")
    elif(computer == 0 and you == 1):
        print("you win !")
    else:
        print("something went wrong!")