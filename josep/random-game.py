import random
num = random.randint(1,100)

print("WITAJ W ZGADUJ ZGADULA!")

guess_list = [0]

while True:
    guess = int(input("Wybierz liczbe od 1 do 100.\n"))
    pass
    if guess < 1 or guess > 100:
        print("Poza zakresem. Sprobuj ponownie.")
        continue
    if guess == num:
        print(f"***Oto ta liczba! Zgadles za {len(guess_list)} razem.")
        break
    guess_list.append(guess)

    if guess_list[-2]:
        if abs(num - guess) < abs(num - guess_list[-2]):
            print("CIEPLEJ!")
        else: print("ZIMNIEJ!")
    else:
        if abs(num - guess) <= 10:
            print("CIPELO!")
        else: print("ZIMNO!")