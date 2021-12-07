play_board = ['spaceholder',' ',' ',' ',' ',' ',' ',' ',' ',' ']
import os, random
os.system("clear")

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

def player_choose_marker():
    marker = ""
    while marker not in ("X", "O"):
        marker = input("Choose X or O: ")
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def put_marker(board, marker, position):
    while position not in range (1,10):
        position = int(input("Choose index 1 - 9: "))
    board[position] = marker

def check_win(board, marker):
        return board[1] == board[2] == board[3] == marker or board[4] == board[5] == board[6] == marker or board[7] == board[8] == board[9] == marker or board[1] == board [4] == board[7] == marker or board[2] == board[5] == board[8] == marker or board[3] == board[6] == board[9] == marker or board[1] == board[5] == board[9] == marker or board[3] == board[5] == board [7] == marker

def whofirst():
    turn = random.randint(0,1)
    if turn == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False

def full_board_check(board):
    for position in range(1,10):
        if space_check(board, position):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Put index 1-9: "))
    return position
    
def replay():
    continue_game = False
    while not (continue_game == "Y" or continue_game == "N"):
        continue_game = input("Do you want to play again? Y or N: ").upper()
    if continue_game == "Y":
        return True
    else:
        return False

print("Tic Tac Toe!")

while True:
    play_board = [" "] * 10
    player1_marker, player2_marker = player_choose_marker()
    turn = whofirst()
    print(turn + ' will go first.')

    # play_game = input('Are you ready to play? Enter Yes or No.')    
    # if play_game.lower()[0] == 'y':
    #     game_on = True
    # else:
    #     game_on = False
    game_on = True
    while game_on:
        if turn == "Player 1":

        # if whofirst() == "Player 1":
            display_board(play_board)
            position = player_choice(play_board)
            put_marker(play_board, player1_marker, position)
            if check_win(play_board, player1_marker) == True:
                os.system("clear")
                display_board(play_board)
                print("Congratulations! Player 1 has won!")
                game_on = False
            else:
                if full_board_check(play_board) == True:
                    os.system("clear")
                    display_board(play_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = "Player 2"
                    os.system("clear")
        else:
        # if whofirst() == "Player 1":
            display_board(play_board)
            position = player_choice(play_board)
            put_marker(play_board, player2_marker, position)
            if check_win(play_board, player2_marker) == True:
                os.system("clear")
                display_board(play_board)
                print("Congratulations! Player 2 has won!")
                game_on = False
            else:
                if full_board_check(play_board) == True:
                    os.system("clear")
                    display_board(play_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = "Player 1"
                    os.system("clear")
    if not replay():
        break