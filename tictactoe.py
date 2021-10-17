#Tic Tac Toe
#Kyiem Chandler
#10/13/2021

from turtle import *
import random
    
    

def displayBoard():
    #Vertical left 
    penup()
    setx(-100)
    sety(-200)
    pendown()
    left(90)
    forward(400)
    #Vertical right
    penup()
    setx(100)
    sety(-200)
    pendown()
    forward(400)

    #Horizontal Top
    penup()
    setx(-225)
    sety(50)
    pendown()
    right(90)
    forward(450)

    #Horizontal Bottom
    penup()
    setx(-225)
    sety(-100)
    pendown()
    forward(450)
    penup()

#Player one is X
def playerOne():
    pendown()
    right(45)
    forward(75)
    penup()
    left(135)
    forward(50)
    pendown()
    left(135)
    forward(75)
    penup()
    #Find a way to make the pointer back like the original pointer for the first x
    right(135)
    forward(55)
    left(270)

#Player 2 is O
def playerTwo():
    pendown()
    circle(40)
    penup()

    
#Prints the players character in the box that they choose
def Choice(playerChoice,turn):
    #X spot dictation
    if turn == 1:
    #Each number correlates to its spot
        if playerChoice == 1:
            setx(-200)
            sety(125)
        
        if playerChoice == 2:
            setx(-35)
            sety(125)
            
        if playerChoice == 3:
            setx(130)
            sety(125)
        
        if playerChoice == 4:
            setx(-200)
            sety(0)
        
        if playerChoice == 5:
            setx(-35)
            sety(0)
           
        if playerChoice == 6:
            setx(130)
            sety(0)
        
        if playerChoice == 7:
            setx(-200)
            sety(-125)
        
        if playerChoice == 8:
            setx(-35)
            sety(-125)
        
        if playerChoice == 9:
            setx(130)
            sety(-125)
            
    #O spot dictation
    if turn == 2:
    #Each number correlates to its spot
        if playerChoice == 1:
            setx(-175)
            sety(100)
        
        if playerChoice == 2:
            setx(0)
            sety(100)
            
        if playerChoice == 3:
            setx(175)
            sety(100)
        
        if playerChoice == 4:
            setx(-175)
            sety(-70)
        
        if playerChoice == 5:
            setx(0)
            sety(-70)
           
        if playerChoice == 6:
            setx(175)
            sety(-70)
        
        if playerChoice == 7:
            setx(-175)
            sety(-200)
        
        if playerChoice == 8:
            setx(0)
            sety(-200)
        
        if playerChoice == 9:
            setx(175)
            sety(-200)
def gameLogic():
    #Dictates randomly who goes first   
    turn = random.randint(1,2)
    win = 'false'
    found = 'false'
    Round = 0
    playerOneSpots = []
    playerTwoSpots = []
    options = [1,2,3,4,5,6,7,8,9]
    i = 0
    aDub1 = 0
    aDub2 = 0
    aDub3 = 0
    aDub4 = 0
    aDub5 = 0
    aDub6 = 0
    aDub7 = 0
    aDub8 = 0
    aDub9 = 0
    aDub10 = 0
    aDub11 = 0
    aDub12 = 0

    
    while win != 'true':
        Round += 1
        if turn == 1:
            playerChoice = int(input("Player one pick between spots one through 9\n"))
            while playerChoice < 0 or playerChoice > 9:
                print("Didn't choose between 0 and 9")
                playerChoice = int(input("Player one pick between spots one through 9\n"))
            while playerChoice >= 0 and playerChoice <= 9:
                for i in range(len(options)):
                    if playerChoice == options[i]:
                        found = 'true'
                        playerOneSpots.append(playerChoice)
                        options.remove(options[i])
                        print(options)
                        print("Player one choices", playerOneSpots)
                        break
                    if found == 'false':
                        playerChoice = int(input("Number has already been chosen. Pick a new number. \n"))
                    break
                break
                #    else:
                #        found = 'false'
               # if found == 'false':
                 #   playerChoice = int(input("Number has already been chosen. Pick a new number. \n"))

                                       

                    
        if turn == 2:
            playerChoice = int(input("Player Two pick between spots one through 9\n"))
            while playerChoice < 0 or playerChoice > 9:
                print("Didn't choose between 0 and 9")
                playerChoice = int(input("Player one pick between spots one through 9\n"))
            while playerChoice >= 0 and playerChoice <= 9:
                for i in range(len(options)):
                    if playerChoice == options[i]:
                        found = 'true'
                        playerTwoSpots.append(playerChoice)
                        options.remove(options[i])
                        print(options)
                        print("Player two choices ",playerTwoSpots)

                        break
                    break
                break
                 #   else:
                     #   found = 'false'
                #if found == 'false':
                   # playerChoice = int(input("Number has already been chosen. Pick a new number. \n"))


                                       
        Choice(playerChoice,turn)
        if turn == 1:
            playerOne()
            turn = turn + 1
        else:
            playerTwo()
            turn = turn - 1
        
        if Round == 9 and win != 'true':
            win = 'true'
            print("Draw: no one wins.")
        if Round >= 5:
            print(playerOneSpots)
            print(playerTwoSpots)
            if len(playerOneSpots) >= 3: 
            #If player one wins
               for i in range(len(playerOneSpots)):
                    if playerOneSpots[i] == 1 or playerOneSpots [i] == 2 or playerOneSpots[i] == 3:
                        aDub1 += 1;
                        if aDub1 == 3:
                            win = 'true'
                            print("Player one wins!1 ",aDub1)
                            setx(-200)
                            sety(100)
                            pendown()
                            forward(400)
                            penup()
                    if playerOneSpots[i] == 1 or playerOneSpots [i] == 5 or playerOneSpots[i] == 9:
                        aDub2 += 1;
                        if aDub2 == 3:
                            win = 'true'
                            print("Player one wins!2 ",aDub2)
                            setx(-170)
                            sety(175)
                            right(45)
                            pendown()
                            forward(600)
                            penup()
                    if playerOneSpots[i] == 1 or playerOneSpots [i] == 4 or playerOneSpots[i] == 7:
                        aDub3 =aDub3 + 1;
                        if aDub3 == 3:
                            win = 'true'
                            print("Player one wins!3 ", aDub3)
                            setx(-170)
                            sety(175)
                            right(90)
                            pendown()
                            forward(400)
                            penup()
                    if playerOneSpots[i] == 2 or playerOneSpots [i] == 5 or playerOneSpots[i] == 8:
                        aDub4 += 1;
                        if aDub4 == 3:
                            win = 'true'
                            print("Player one wins! ",aDub4)
                    if playerOneSpots[i] == 3 or playerOneSpots [i] == 6 or playerOneSpots[i] == 9:
                        aDub5 += 1;
                        if aDub5 == 3:
                            win = 'true'
                            print("Player one wins! ", aDub5)
                    if playerOneSpots[i] == 3 or playerOneSpots [i] == 5 or playerOneSpots[i] == 7:
                        aDub6 += 1;
                        if aDub6 == 3:
                            win = 'true'
                            print("Player one wins! ", aDub6)

                
            if(len(playerTwoSpots) >= 3):
            #If player two wins
               for i in range(len(playerTwoSpots)):
                    if playerTwoSpots[i] == 1 or playerTwoSpots [i] == 2 or playerTwoSpots[i] == 3:
                        aDub7 += 1;
                        if aDub7 == 3:
                            win = 'true'
                            print("Player two wins!", aDub7)
                            setx(-200)
                            sety(100)
                            pendown()
                            forward(400)
                            penup()
                    if playerTwoSpots[i] == 1 or playerTwoSpots [i] == 5 or playerTwoSpots[i] == 9:
                        aDub8 += 1;
                        if aDub8 == 3:
                            win = 'true'
                            print("Player two wins!", aDub8)
                            setx(-200)
                            sety(100)
                            right(35)
                            pendown()
                            forward(400)
                            penup()
                    if playerTwoSpots[i] == 1 or playerTwoSpots [i] == 4 or playerTwoSpots[i] == 7:
                        aDub9 += 1;
                        if aDub9 == 3:
                            win = 'true'
                            print("Player two wins!", aDub9)
                            setx(-200)
                            sety(100)
                            right(90)
                            pendown()
                            forward(400)
                            penup()
                    if playerTwoSpots[i] == 2 or playerTwoSpots [i] == 5 or playerTwoSpots[i] == 8:
                        aDub10 += 1;
                        if aDub10 == 3:
                            win = 'true'
                            print("Player two wins!", aDub10)
                    if playerTwoSpots[i] == 3 or playerTwoSpots[i] == 6 or playerTwoSpots[i] == 9:
                        aDub11 += 1;
                        if aDub11 == 3:
                            win = 'true'
                            print("Player two wins!", aDub11)
                    if playerTwoSpots[i] == 3 or playerTwoSpots [i] == 5 or playerTwoSpots[i] == 7:
                        aDub12 += 1;
                        if aDub12 == 3:
                            win = 'true'
                            print("Player two wins!", aDub12)



                
    
displayBoard()
gameLogic()




