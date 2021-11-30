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


board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(board)

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
# player_input()

position = 10

def place_marker(board, marker, position):
    while position not in range(1, 10):
        position = int(input("Please choose a position index (1 - 9): "))
    # marker tutaj bedzie do zmiany, naprzemiennie XOXOXOXOX
    marker = "X"
    board[position] = marker
    # do zrobienia counter dla naprzemiennych tur
    # counter += counter
    display_board(board)

# place_marker(board, "%", position)

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


import random
def choose_first():
    going_first = random.randint(1,2)
    if going_first == 1:
        return "Player 1"
        # print("P1")
    else:
        return "Player 2"
        # print("P2")

# choose_first()

def space_check(board, position):
    for space in board:
        # jesli nie rowna sie ani X ani O, to znaczy ze jest puste -> prawda ze mozna grac dalej
        if space != "X" or space != "O":
            return True
        else:
            return False

space_check(board, position)
