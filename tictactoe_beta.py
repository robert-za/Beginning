# import os
# os.system('clear')


# from os import stat_result


def display_board(board):
    print("|---------|---------|---------|")
    print("|         |         |         |")
    print("|    "+board[7]+"    |    "+board[8]+"    |    "+board[9]+"    |")
    print("|         |         |         |")
    print("|---------|---------|---------|")
    print("|---------|---------|---------|")
    print("|         |         |         |")
    print("|    "+board[4]+"    |    "+board[5]+"    |    "+board[6]+"    |")
    print("|         |         |         |")
    print("|---------|---------|---------|")
    print("|---------|---------|---------|")
    print("|         |         |         |")
    print("|    "+board[1]+"    |    "+board[2]+"    |    "+board[3]+"    |")
    print("|         |         |         |")
    print("|---------|---------|---------|")


board = ['#','X','O','X','O','X','O','X','O',' ']
# display_board(board)

import random
def choose_first():
    # if going_first == 1:
    #     return True
    #     # print("P1")
    # else:
    #     return False
    #     # print("P2")
    return random.randint(0,1)

# choose_first()

def player_input():

    choice = "wrong"
    xo = ["X", "O"]
    while choice not in xo:
        choice = input("Player 1, please choose side (X or O):\n")
    if choice == "X":
        xo.pop(0)
    else:
        xo.pop(1)
    player2 = xo[0]
    print(f"Player 1 is now {choice} and Player 2 is {player2}.")
player_input()



position = 0
# marker = ["O", "X"]
turn_number = 0

def place_marker(board, marker, position):
    position = "Wrong"
    while position not in range(1, 10):
        position = int(input("Please choose a position index (1 - 9): "))
    # marker tutaj bedzie do zmiany, naprzemiennie XOXOXOXOX
    # print(position, "TUTAJ SPRAWDZAM CO DAJE")
    
    if choose_first() == False:
        


    
    board[position] = marker
    # do zrobienia counter dla naprzemiennych tur
    # counter += counter
    display_board(board)
    # print(position, "TUTAJ SPRAWDZAM CO DAJE")
    # print(position2, "TUTAJ SPRAWDZAM CO DAJE")
    # turn_number += turn_number
    return position, marker

# position = place_marker(board, marker, position)

place_marker(board, "%", position)

def win_check(board, marker):
    check_status = False
    if board[1] == board[2] == board[3] == marker:
        check_status = True
    elif board[4] == board [5] == board[6] == marker:
        check_status = True
    elif board[7] == board[8] == board[9] == marker:
        check_status = True
    elif board[1] == board[4] == board[7] == marker:
        check_status = True
    elif board[2] == board[5] == board[8] == marker:
        check_status = True
    elif board[3] == board[6] == board[9] == marker:
        check_status = True
    elif board[1] == board[5] == board[9] == marker:
        check_status = True
    elif board[3] == board[5] == board[7] == marker:
        check_status = True
    else:
        check_status = False
    return check_status

# win_check(board, "X")




def space_check(board):
    if board[position] == "X" or board[position] == "O":
        # print("False + w positon jest albo X albo O", position)
        return False
    else:
        # print("True + w position nie ma X ani O", position)
        return True

# space_check(board)

def full_board_check(board):
    if " " in board:
        # print("True + gdzies w board znajduje sie puste")
        return True
    else:
        # print("False + w board nie ma pustego")
        return False

full_board_check(board)

next_step2 = 0

def player_choice(board):
    next_step = "Wrong"
    while next_step not in range(1,10):
        next_step = int(input("What is the next move? (1 - 9): "))
    if space_check(board) == True:
        board[position] = next_step
    else:
        while next_step not in range(1,10):
            next_step = int(input("What is the next move? (1 - 9): ")) 
    global next_step2; next_step2 = next_step
    return next_step2

marker = "X"

def replay():
    game_on = False
    if win_check(board, marker) == False and full_board_check() == False:
        print("would you like to play another one? (Y or N)")



replay()
    

def check_tie():
    pass
