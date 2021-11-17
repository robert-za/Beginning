counter = 0
word = input("pick a secret word\n")
while counter != -1:
    word = input()
    if word == "Franek":
        print("You've successfully left the loop.")
        break
    else:
        counter += 1
