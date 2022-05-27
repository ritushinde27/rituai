# One player and one bot tic tac toe game using AI

# Making the board and defining the postions on the board
# 1|2|3
# 4|5|6
# 7|8|9



board = {1: ' ',2: ' ',3: ' ',
         4: ' ',5: ' ',6: ' ',
         7: ' ',8: ' ',9: ' '}

# Printing the board at a current stage
def printBoard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('\n')


def isSpaceFree(position):
    if(board[position]==' '):
        return True
    else:
        return False

def checkForDraw():
    for key in board.keys():
        if(board[key]==' '):
            return False
    return True    
    



def checkForWin():
    if(board[1] == board[2] and board[1]==board[3] and board[1]!=' '):
        return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4]!=' '):
        return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7]!=' '):
        return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1]!=' '):
        return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2]!=' '):
        return True
    elif(board[3]==board[6] and board[3]==board[9] and board[3]!=' '):
        return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1]!=' '):
        return True
    elif(board[7]==board[5] and board[7]==board[3] and board[7]!=' '):
        return True
    else:
        return False
    

def checkWhichMarkWon(mark):
    if(board[1] == board[2] and board[1]==board[3] and board[1]==mark):
        return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4]==mark):
        return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7]==mark):
        return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1]==mark):
        return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2]==mark):
        return True
    elif(board[3]==board[6] and board[3]==board[9] and board[3]==mark):
        return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1]==mark):
        return True
    elif(board[7]==board[5] and board[7]==board[3] and board[7]==mark):
        return True
    else:
        return False


def insertLetter(letter,position):
    if(isSpaceFree(position)):
        board[position]=letter
        printBoard(board)
        if(checkForDraw()):
            print("DRAW!")
            exit()
        if(checkForWin()):
            if(letter=='X'):
                print("The Bot wins")
                exit()
            else:
                print("You Won!!!!!")
                exit()
        return 



    else:
        print('This position is alread filled. Try again')
        position = int(input("Enter new postion: "))
        insertLetter(letter,position)
        return

player = 'O'
bot = 'X'

printBoard(board)
# insertLetter('X',1)
# insertLetter('X',2)
# insertLetter('X',3)


def playerMove():
    position = int(input("Enter the position for 'O': "))
    insertLetter(player,position)
    return



def botMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score = minimax(board,0,False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot,bestMove)
    return 


def minimax(board,depth,isMaximizing):
    if(checkWhichMarkWon(bot)):
        return 100
    elif(checkWhichMarkWon(player)):
        return -100
    elif(checkForDraw()):
        return 0
    
    if(isMaximizing):
        bestScore = -1000

        for key in board.keys():
            if(board[key]==' '):
                board[key]=bot
                score = minimax(board,0,False)
                board[key] = ' ' 
                if(score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore=800

        for key in board.keys():
            if(board[key]==' '):
                board[key]=player
                score = minimax(board,0,True)
                board[key] = ' '
                if(score < bestScore):
                    bestScore = score
        return bestScore


        
    




while not checkForWin():
    botMove()
    playerMove()
    # playerMove()
    # botMove()
    





