# import os
# os.system('clear')

from os import stat_result


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


board = ['#','X','X','X','O','X','O','X','O','X']
display_board(board)

def player_input():
    choice = "wrong"
    xo = ["X", "O"]
    while choice not in xo:
        choice = input("Player 1, please choose side (X or O):\n")
    if choice == "X":
        xo.pop(0)
    else:
        xo.pop(1)
    player2_marker = xo[0]
    print(f"Player 1 is now {choice} and Player 2 is {player2_marker}.")
player_input()

position = 10

def place_marker(board, marker, position):
    while position not in range(1, 10):
        position = int(input("Please choose a position index (1 - 9): "))
    # marker tutaj bedzie do zmiany, naprzemiennie XOXOXOXOX
    marker = "%"
    board[position] = marker
    # do zrobienia counter dla naprzemiennych tur
    # counter += counter
    display_board(board)

place_marker(board, "%", position)

def win_check(board, mark):
    check_status = False
    if board[1] == board[2] == board[3]:
        check_status = True
        return mark
    elif board[4] == board [5] == board[6]:
        check_status = True
        return mark
    elif board[7] == board[8] == board[9]:
        check_status = True
        return mark
    elif board[1] == board[4] == board[7]:
        check_status = True
        return mark
    elif board[2] == board[5] == board[8]:
        check_status = True
        return mark
    elif board[3] == board[6] == board[9]:
        check_status = True
        return mark
    elif board[1] == board[5] == board[9]:
        check_status = True
        return mark
    elif board[3] == board[5] == board[7]:
        check_status = True
        return mark
    else:
        check_status = False
    print(check_status)
    # ta funkcja nic mi nie zwraca na te chwile
    # return check_status

win_check(board, "X")

