# Neil's Grocery Store Game
# Written by Neil Fink, 2021

import random

def generate_store():
   
    return 0
    
def runGame(gameType):
    if gameType == 1:
        game1()
    elif gameType == 2:
        game2()
    else:
        game3()
        
def game1():
    print("Playing game 1!")
    
    
    
    return 0

def game2():
    print("Playing game 2!")
    
    
    
    return 0

def game3():
    print("Playing game 3!")
    
    
    
    return 0

def runOptions():
    print("Running options!")
    
# Main loop
gameEnd = False
print("Welcome to NeilMart!\nWhat would you like to do?")
while not gameEnd:
    print("[1] - Game 1, [2] - Game 2, [3] - Game 3, [4] - Options, [5] - Exit")
    try:
        userInput = int(input("Enter choice: "))
    except ValueError:
        userInput = 0
        
    if userInput >=1 and userInput <=3:
        runGame(userInput)
        userInput = 0
        while userInput <1 or userInput >2:
            try:
                userInput = int(input("Play again? [1]yes, [2]no: "))
            except ValueError:
                userInput = 0
    
        if userInput == 2:
            gameEnd = True
            
    elif userInput == 4:
        runOptions()
        
    elif userInput == 5:
        gameEnd = True
