import pandas
abc = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter:row.code for (index, row) in abc.iterrows()}

user_word = input("What's the word to translate to NATO code?: ").upper()
while True:
    try:
        output_list = [alphabet[letter] for letter in user_word]
    except KeyError:
        print("sorry, not a word")
        user_word = input("What's the word to translate to NATO code?: ").upper()
    else:
        print(output_list)
        break