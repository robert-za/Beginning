#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = (names_file.readlines())

with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
        contents = starting_letter.read()
for name in names:
    clear_name = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_for_{clear_name}.txt", mode = "w") as file:
        file.write(contents.replace("[name]", clear_name))