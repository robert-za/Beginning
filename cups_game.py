from random import shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2. \n")
    return int(guess)

def check_guess(my_list, guess):
    if my_list[guess] == "O":
        print("Correct!")
    else: 
        print("Wrong guess!")
        print(my_list)
    return

my_list = [" ", "O", " "]
mixlist = shuffle_list(my_list)
guess = player_guess()
check_guess(mixlist,guess)