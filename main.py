#Create a program that simulates rock, paper, scissors!
from random import randint

again = ""

def Rochambeau(x,y):
    print("The computer has chosen", y, ".")
    if x == y: print("It's a tie!"),
    elif (x=="rock" and y == "paper") or (x=="paper" and y=="rock") : print ("Paper beats rock!"),
    elif (x=="rock" and y =="scissors") or (x=="scissors" and y=="rock") : print("Rock beats scissors!"),
    elif (x=="paper" and y=="scissors") or (x=="scissors" and y=="paper") : print("Scissors beat rock!"),



while again!="no" :
    x=(input("Please enter rock, paper, or scissors "))
    x=(x).lower()
    y=randint(1,3)
    if y==1: y="paper"
    elif y==2: y="rock"
    elif y==3: y="scissors"

    Rochambeau(x,y)
    again = input("Would you like to play again?")
    again = again.lower()

print("Okay, have a great rest of your day!")


