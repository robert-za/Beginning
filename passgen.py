#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password_string = ''
password_list = []
for i in range(1, nr_letters + 1):
    number_letter = random.randint(0, len(letters) - 1)
    # print(letters[number])
    # password += letters[number_letter]
    password_list.append(letters[number_letter])

for j in range (1, nr_symbols + 1):
    number_symbol = random.randint(0, len(symbols) - 1)
    # password += symbols[number_symbol]
    password_list.append(symbols[number_symbol])

for k in range (1, nr_numbers + 1):
    number_number = random.randint(0, len(numbers) - 1)
    # password += numbers[number_number]
    password_list.append(numbers[number_number])

# print(password_list)
random.shuffle(password_list)
# print(password_list)
# print(type(password_list))
# print(type(password_list[0]))
# password_random = str(password_list) 
password = ''.join(password_list)
print(password)
# print(password_random)
# password_random = password.shuffle()

# print(random_password)

# print(password)