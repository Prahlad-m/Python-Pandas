##Tic Tac Toe

import random

board = [["1","2","3"],["4","5","6"],["7","8","9"]]

#checkSame returns True if all the values in a list are the same,
#ie, one unique value in the set. (x,x,x) or (o,o,o).
def checkSame(List):
    return len(set(List)) == 1

def displayBoard(board):
    for i in board:
        print(i)
    return

def checkVictory(board):

    #check rows
    for i in range(3):
        if checkSame(board[i]):
            return True, board[i][0]
    #check columns
    for i in range(3):
        boardColumn = [board[0][i],board[1][i],board[2][i]]
        if checkSame(boardColumn):
            return True, board[0][i]
    #check diagonals
    boardDiagOne = [board[0][0],board[1][1],board[2][2]]
    if checkSame(boardDiagOne):
        return True, board[0][0]
    boardDiagTwo = [board[0][2],board[1][1],board[2][0]]
    if checkSame(boardDiagTwo):
        return True, board[0][2]

    #check for stalemate
    Set = []
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                Set.append(board[i][j])
    if len(Set) == 0:
        return True, "-"
    return False, "0"

def checkPosition(board, value):
    for i in range(3):
        if value in board[i]:
            return True
    return False

def makeMove(board, value, turn):
    for i in range(3):
        if value in board[i]:
            for j in range(3):
                if value == board[i][j]:
                    board[i][j] = turn
    return board

def isValid(value):
    if value.isdigit() == False:
        return False
    if (1 <= int(value) <= 9) == False:
        return False
    if checkPosition(board, value) == False:
        return False
    return True

def playerMove(board):
    while 1:
        value = str(input("('o').Please enter a valid position: "))
        if isValid(value):
            return value
        else:
            print("Invalid position.")

def computerMove(board):
    Set = []
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                Set.append(board[i][j])
    move = Set[(random.randint(1,len(Set)))-1]
    return move


#Game
print("Naughts and Crosses!!")
print("You, the player, are 'o', and the computer is 'x'.")
print("The game begins!!")
displayBoard(board)
turn = 1
victory = False

while victory == False:
    if turn == 1:
        print("Computer turn!")
        value = computerMove(board)
        print("Computer chooses ",value,".")
        makeMove(board, value, 'x')

        turn = 0

    elif turn == 0:
        print("Player turn!")
        value = playerMove(board)
        print("Player chooses ",value,".")
        makeMove(board, value, 'o')

        turn = 1

    displayBoard(board)
    victory, winner = checkVictory(board)

if winner == 'x':
    print("Commiserations! The computer is the winner!!")
elif winner == 'o':
    print("Congratulations! The player is the winnner!!")
elif winner == '-':
    print("Stalemate! No winners!!")
    



