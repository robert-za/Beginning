theBoard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
test_board = ['#','O','O',' ','O','X','O','X','O','X']
import os

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

def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def place_marker(board, marker, position):
    while position not in range (1,10):
        position = int(input("Choose index 1 - 9: "))
    board[position] = marker

def win_check(board, mark):
    # check_status = False
    return board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == board[9] == mark or board[1] == board [4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == mark or board[3] == board[5] == board [7] == mark


    # if board[1] == board[2] == board[3] == mark:
    #     check_status = True
    # elif board[4] == board [5] == board[6] == mark:
    #     check_status = True
    # elif board[7] == board[8] == board[9] == mark:
    #     check_status = True
    # elif board[1] == board[4] == board[7] == mark:
    #     check_status = True
    # elif board[2] == board[5] == board[8] == mark:
    #     check_status = True
    # elif board[3] == board[6] == board[9] == mark:
    #     check_status = True
    # elif board[1] == board[5] == board[9] == mark:
    #     check_status = True
    # elif board[3] == board[5] == board[7] == mark:
    #     check_status = True
    # else:
    #     check_status = False
    # print(check_status)
    # return check_status

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    if board[position] == "X" or board[position] == "O":
        return False
    else:
        return True


def full_board_check(board):
    for position in range(1,10):
        if space_check(board, position):
            return False
    return True

# def player_choice(board):
#     position = 0
#     while position not in range (1,10):
#         position = int(input("Choose index 1 - 9: "))
#         #IF SPACE IS EMPTY, RETURN ITS INDEX
#         while space_check(board, position) == True:
#             return position

def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    continue_game = False
    while not (continue_game == "Y" or continue_game == "N"):
        continue_game = input("Do you wanna play again? Y or N: ").upper()
    if continue_game == "Y":
        return True
    else:
        return False

print("Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    os.system('clear')

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    os.system('clear')

    if not replay():
        break