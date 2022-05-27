import random
import sys
from random import randint
computer_turn_counter = 0

def printBoard(board):
    print(' ' + board[1] + ' |' + board[2] + ' |' + board[3])
    print(' ' + board[4] + ' |' + board[5] + ' |' + board[6])
    print(' ' + board[7] + ' |' + board[8] + ' |' + board[9])
  

def isSpaceFree(board, move):
    if board[move] == ' ':
        return True
    else:
        False 

def my_custom_random(takenmoves):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    allmoves = [1,2,3,4,5,6,7,8,9]
    movesList = list(set(allmoves) - set(takenmoves))
    return random.choice(movesList)

def updateMove(board, letter , move):
    board[move] = letter

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def getComputersMove(board, computerletter, playerletter, dict ,list, computer_turn_counter):

    global magicboard
    checkforplayer = 0
    print("Comp Turns Completed : ",computer_turn_counter)
    #If First Time 
    if (computer_turn_counter == 0):
        move = my_custom_random(list )
        computer_turn_counter=+1
        return move , computer_turn_counter
    
    #Second Time
    if (computer_turn_counter == 1):
        computer_turn_counter= 2
        #try to get middle element
        if (isSpaceFree(board,5)):
            move = 5
            return 5 , computer_turn_counter
        else:
           
            checkforplayer = 1
    
    #Checks self wining chances
    if (computer_turn_counter and len(dict[computerletter]) > 1 ):
        print("|| In self wining chances ")
        computer_turn_counter=3
        length = len(dict[computerletter]) 
        for i in range(0,length - 1):
            #Formula 
            diff = 15 - (magicboard[ dict[computerletter][i] -1 ] + magicboard[ dict[computerletter][length - 1] - 1 ])
            print("The Diff: 15 - (",magicboard[ dict[computerletter][i] -1 ] ," + ",magicboard[ dict[computerletter][length - 1] - 1 ],"): " ,diff)
            
            if(diff in magicboard):
              
                checkforplayer = 1
            else:
                checkforplayer = 1
                continue
            

            index = magicboard.index(diff) + 1
            print("The Index to be placed at is : ", index )
            if (index <= 9 and index > 0):
                if isSpaceFree(board, index) :
                    print("Returned the Difference in self win")
                    return index  , computer_turn_counter
                else:
                    print("Cant Add , Position is Taken Already")
                    checkforplayer = 1
            else : 
                checkforplayer = 1

    #Checks to Defeat the Player
    if checkforplayer == 1:
        print("|| In Defeat the Player ")
        length = len(dict[playerletter]) 
        for i in range(0,length - 1):
            #Formula 
            diff = 15 - (magicboard[ dict[playerletter][i] -1 ] + magicboard[ dict[playerletter][length - 1] - 1 ] )
            print("The Diff: 15 - (",magicboard[ dict[playerletter][i] -1 ] ," + ",magicboard[ dict[playerletter][length - 1] - 1 ],"): " ,diff)
            
            if(magicboard.index(diff)):
                if(magicboard.index(diff) > 9 or magicboard.index(diff) <= 0):
                    checkforplayer = 1
                    continue

            index = magicboard.index(diff) + 1
            print("The Index to be placed at is : ", index )
            if (index <= 9 and index > 0):
                if isSpaceFree(board, index) :
                    print("Returned the Difference defeat player")
                    return index , computer_turn_counter
                else:
                    print("Cant Add , Position is Taken Already")
                    checkforplayer = 1
            else : 
                checkforplayer = 1
        

    
    computer_turn_counter = computer_turn_counter + 1
    return my_custom_random(list) , computer_turn_counter
    
def isWinner(bo, le):
     # Given a board and a player’s letter, this function returns True if that player has won.
     # We use bo instead of board and le instead of letter so we don’t have to type as much.
     return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
     (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
     (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
     (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
     (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
     (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
     (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
     (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    
    

def makechoice():
    #TicTacToe()
    
    x = 1

    while(x):
        choice = input("Choose your Player X or O : ")

        if choice =="x" or choice=="X":
            print("Player has chosen X and will go First\n")
            x = 0
            playerletter = "X"
            computerletter = "O"
            turn = "player"
        elif choice =="O" or choice=="o":
            print("Player has chosen O , Bot will go First\n")
            x = 0
            playerletter = "O"
            turn = "computer"
            computerletter = "X"
        else:
            print("Not an option, IDIOT. Choose again.\n")

    return playerletter,computerletter,turn 
        
def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True



magicboard = [8,3,4,
              1,5,9,
              6,7,2]
dict = {
    "X":[],
    "O":[]
}
LIST = []
board = [' '] * 10

playerletter,computerletter,turn = "X", "O", "player"

#playerletter,computerletter,turn = makechoice()
gamePlaying = True  

while gamePlaying:
    if turn =="player":
        #Player’s turn.
        printBoard(board)
        move = getPlayerMove(board)
        dict[playerletter].append(move )
        LIST.append(move)
        print(dict)
        updateMove(board,playerletter,move)

        if isWinner(board, playerletter):
               printBoard(board)
               print('****************** Hooray! You have won the game! ******************')
               sys.exit("Thank You For Playing!") 
               gameIsPlaying = False

        else:
            if isBoardFull(board):
                print('****************** The game is a tie! ****************** ')
                printBoard(board)
                sys.exit("Thank You For Playing!")
                break
            else:
                   turn = 'computer'
    else:
        #Computer's Turn
        move , computer_turn_counter = getComputersMove(board,computerletter ,playerletter, dict ,LIST , computer_turn_counter)
        dict[computerletter].append(move )
        LIST.append(move)
        print(dict)
        updateMove(board,computerletter,move)
        if isWinner(board, computerletter):
            printBoard(board)
            print('You Lost to a bOt! .')
            sys.exit("Thank You For Playing!")
            gameIsPlaying = False
        else:
            if isBoardFull(board):
                board(board)
                print('The game is a tie!')
                break
            else:
                turn = 'player'
    


