#Tic Tac Toe
#Kyiem Chandler
#10/13/2021

from turtle import *
import random

board = [' ' for x in range(10)]

def printConsoleBoard(board):
    print('    |   |')
    print('  '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('    |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    |   |')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |   |')




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

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '


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
    return 'X'

def playerTwo():
    pendown()
    circle(40)
    penup()
    return 'O'



def Choice(playerChoice,turn):
    #X spot dictation
    if turn == 1:
    #Each number correlates to its spot
        if playerChoice == 1:
            setx(-200)
            sety(125)
            playerOne()
        if playerChoice == 2:
            setx(-35)
            sety(125)
            playerOne()
        if playerChoice == 3:
            setx(130)
            sety(125)
            playerOne()
        
        if playerChoice == 4:
            setx(-200)
            sety(0)
            playerOne()
       
        if playerChoice == 5:
            setx(-35)
            sety(0)
            playerOne()
           
        if playerChoice == 6:
            setx(130)
            sety(0)
            playerOne()
        
        if playerChoice == 7:
            setx(-200)
            sety(-125)
            playerOne()
        
        if playerChoice == 8:
            setx(-35)
            sety(-125)
            playerOne()
        
        if playerChoice == 9:
            setx(130)
            sety(-125)
            playerOne()
            
    #O spot dictation
    if turn == 2:
    #Each number correlates to its spot
        if playerChoice == 1:
            setx(-175)
            sety(100)
            playerTwo()

        if playerChoice == 2:
            setx(0)
            sety(100)
            playerTwo()
            
        if playerChoice == 3:
            setx(175)
            sety(100)
            playerTwo()
        
        if playerChoice == 4:
            setx(-175)
            sety(-70)
            playerTwo()
        
        if playerChoice == 5:
            setx(0)
            sety(-70)
            playerTwo()
           
        if playerChoice == 6:
            setx(175)
            sety(-70)
            playerTwo()
       
        if playerChoice == 7:
            setx(-175)
            sety(-200)
            playerTwo()
       
        if playerChoice == 8:
            setx(0)
            sety(-200)
            playerTwo()
        
        if playerChoice == 9:
            setx(175)
            sety(-200)
            playerTwo()
   

def playerMove():
    move = 0
    run = True
    while run:
        move = int(input("Please choose a position (1-9). "))
        try:
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    playerChoice = move
                    insertLetter('X', move)
                else:
                    print("Spot chosen already")
            else:
                print("Insert number from 1-9")
        except: 
            print("Type a number.")
    
    return move

def isWinner(board, le):
    return (board[1] == le and board[2] == le and board[3] == le) or (board[4] == le and board[5] == le and board[6] == le) or (board[7] == le and board[8] == le and board[9] == le) or (board[1] == le and board[5] == le and board[9] == le) or (board[3] == le and board[5] == le and board[7] == le) or (board[1] == le and board[4] == le and board[7] == le) or (board[2] == le and board[5] == le and board[8] == le) or (board[3] == le and board[6] == le and board[9] == le)
        
def cpuMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move
    
    cornerOpen = []
    for i in possibleMoves:
        if i in (1,3,7,9):
            cornerOpen.append(i)
        if len(cornerOpen) > 0:
            move = selectRandom(cornerOpen)
    if 5 in possibleMoves:
        move = 5
        return move
    edgeOpen = []
    for i in possibleMoves:
        if i in (2,4,6,8):
            edgeOpen.append(i)
        if len(edgeOpen) > 0:
            move = selectRandom(edgeOpen)

    return move

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]





def BoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    turn = 1
    print("Tic Tac Toe Game")
    printConsoleBoard(board)
    displayBoard()

    while not(BoardFull(board)):
        if not(isWinner(board, 'O')):
            move = playerMove()
            printConsoleBoard(board)
            Choice(move, turn)
            turn = turn + 1
        else: 
            print("O wins.")
            break
        if not(isWinner(board, 'X')):
            move = cpuMove()
            if move == 0:
                print("Tie Game")
            else:
                insertLetter('O', move)
                print("CPU chose ", move)
                printConsoleBoard(board)
                Choice(move, turn)
                turn = turn - 1
        else: 
            print("X wins.")
            break

    if BoardFull(board):
        print("Tie Game.")

main()
