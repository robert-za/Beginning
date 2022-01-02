#clean version with funcs
import random, os

def check_number(guess, number, turns):
    if guess < number:
        print("secret number is higher")
        turns -= 1
        print(f"You have {turns} lives remaining.")
    elif guess > number:
        print("secret number is lower")
        turns -= 1
        print(f"You have {turns} lives remaining.")
    else:
        print(f"Congratulations. The number is: {number}.")
    return turns

def set_difficulty():
    difficulty_list = ["easy", "hard"]
    difficulty = "_"
    while difficulty not in difficulty_list:
        difficulty = input("Do you choose 'hard' or 'easy' mode?: ")
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    return lives

def game():
    os.system("clear")
    print("Welcome to the high/low guess game!\nI'm thinking about a number" 
    " between 1 and 100.")
    the_number = random.randint(1,10)
    player_guess = ""
    lives = set_difficulty()
    while lives > 0 and player_guess != the_number:
        player_guess = int(input("Guess a number: "))   
        lives = check_number(player_guess, the_number, lives)

game()
print("Program will now end")