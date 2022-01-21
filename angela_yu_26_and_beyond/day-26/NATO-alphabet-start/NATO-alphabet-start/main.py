import pandas
abc = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in abc.iterrows():
    # print(row.letter, row.code)
alphabet = {row.letter:row.code for (index, row) in abc.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("What's the word to translate to NATO code?: ").upper()
output_list = [alphabet[letter] for letter in user_word]
print(output_list)


# for (letter, code) in alphabet.items():
#     print(letter, code)