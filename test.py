from random import randrange
randomNumber=randrange(1,3)
userInput=int(input("guess : "))
if userInput==randomNumber:
    print("you won")
else :
    print("you lost the number was: ", randomNumber)