import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

print("WELCOME TO THE HANGMAN!")

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word_hidden = []
for letter in chosen_word:
    chosen_word_hidden.append("_")

word_present = " ".join(chosen_word_hidden)
print(word_present, "\n")

game_on = True

list_of_letters = list(chosen_word)

lives = 6

while game_on:

    guess = input("Choose a letter: ").lower()
    counter = 0

    for letter in list_of_letters:
        if guess == letter:
            chosen_word_hidden[counter] = letter
            counter += 1
        else:
            counter += 1
    
    if guess not in list_of_letters:
        lives -= 1

    word_present = " ".join(chosen_word_hidden)
    print(word_present, "\n")
    print(stages[lives])
    print(f"Remaining lives: {lives}" + 45 * "\n")

    if "_" not in chosen_word_hidden:
        print("You win.\n")
        game_on = False
    
    if lives == 0:
        print("You lose.")
        game_on = False