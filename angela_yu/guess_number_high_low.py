import random, os

os.system("clear")
print("Welcome to the high/low guess game!\nI'm thinking about a number" 
" between 1 and 100.")

the_number = random.randint(1,10)
difficulty_list = ["easy", "hard"]
difficulty = ""

while difficulty not in difficulty_list:
    difficulty = input("Do you choose 'hard' or 'easy' mode?: ")
if difficulty == "easy":
    lifes = 10
else:
    lifes = 5



player_guess = ""
game_on = True

while game_on:
    player_guess = int(input("Guess a number: "))
    if player_guess < the_number:
        # check_lifes(game_on)
        print("secret number is higher")
        lifes -= 1
        if lifes == 0:
            game_on = False
        print(f"lifes remaining: {lifes}")
    elif player_guess > the_number:
        # check_lifes(game_on)
        print("secret number is lower")
        lifes -= 1
        if lifes == 0:
            game_on = False
        print(f"lifes remaining: {lifes}")
    else:
        print(f"Congratulations. The number is: {the_number}. You win with {lifes}" 
        " lifes remaining.")
        game_on = False