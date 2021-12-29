# EX2

# prev_num = 0


# print("Printing current and previous number sum in range(10) ")
# for i in range(10):
#     # if i == 0:
#     #     print("Current number", i,"Previous number" ,i ,"Sum:" , i)
#     # else:
#     #     i = i+(i-1)
#     #     print("Current number", i, "Previous number", (i-1), "Sum:", i)
#     print("Current number: ", i, "Previous number: ", prev_num, "Sum: ", i + prev_num)
#     prev_num = i

# EX 3
# my_string = input("Put a string: \n")
# for i in range(len(my_string)):
#     if i % 2 == 0:
#         print(my_string[i])
# # for i in my_string:
# #     if i % 2 == 0:
# #         print(i)

# for i in list(my_string)[0::2]:
#     print(i)

# Ex4
# def remove_chars():
#     my_string = input("Gib a string: ")
#     # my_list = list(my_string)
#     n = int(input("Gib n: "))
#     # my_list.pop() * n
#     my_string = my_string[n::]
#     print(my_string)

# remove_chars()

# EX6
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# if numbers_y[0] == numbers_y[len(numbers_y)-1]:
#     print(True)
# else:
#     print(False)
# '''
# komentuje
# '''

# print("I have eaten",99,"burritos.")
# false
# false
# true
# false
# false
# true < > == <= >= !=

# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!")

# for i in range(1,11):
    # print(i)
# i = 1
# while i < 11:
#     print(i)
#     i += 1













# def collatz(number):
#     if number % 2 == 0:
#         print(number//2)
#         return number//2
#     else:
#         print(3*number+1)
#         return (3*number+1)

# while True:
#     try:
#         while True:
#             user_number = int(input("give a number: "))
#             print(user_number)
#             while user_number > 1:
#                 user_number = collatz(user_number)
#             break
#         break
#     except ValueError:
#         print("this is not a number")
        











# cat_names = []
# while True:
#     print("Enter the name of a cat " + str(len(cat_names) +1 ) + \
#     "(Or enter nothing to stop.):")
#     name = input()
#     if name == "":
#         break
#     cat_names = cat_names + [name]
# print("The cat names are:")
# for name in cat_names:
#     print("    " + name)


# spam = ["apples", "bananas", "tofu", "cats", "mary", "cactus"]
# spam1 = []

# def list_thing(words):
#     if words == []:
#         print("empty")
#     elif len(words) == 1:
#         print(words[0])
#     else:    
#         print('{} and {}'.format(', '.join(words[:-1]), words[-1]))

# list_thing(spam)



























# import random
# numberOfStreaks = 0
# streak = 0
# my_list = []
# test = 0

# for experimentNumber in range(10000):
#     # Code that creates a list of 100 'heads' or 'tails' values.
#     my_list = []
#     for i in range(100):
#         my_list.append(random.randint(0,1))


#     # Code that checks if there is a streak of 6 heads or tails in a row.
#     for j in range(len(my_list)):
#         if j == 0:
#             pass
#         elif my_list[j] == my_list[j-1]:
#             streak += 1
#         else:
#             streak = 0

#         if streak == 6:
#             numberOfStreaks += 1
#             streak = 0

# print('Chance of streak: %s%%' % (numberOfStreaks / 100))





























# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# counter = 0
# # for i in range(len(grid)):
# #     for j in range(len(grid)):
# #         print(grid[i-1][j-1])
# print("$$$$$$$$$$$$$")
# for j in range(len(grid[0])):
#     print("$$",end="")
#     for i in range(len(grid)):
#         # if i == i:
#         #     print(grid[j][i],end="")
#         # else:
#         #     print(grid[j][i],end="\n")
#         # if j == 0:
#         print(grid[i][j],end="")
#             # counter += 1
#         # else:
#             # print(counter)
#     print("$$")
# print("$$$$$$$$$$$$$")






# figures = ["king", "queen", "rook", "bishop", "knight", "pawn"]
# chess_dict = {"1h":"bking", "6c":"wqueen", "2g":"bbishop", "5h":"bqueen", "3e":"wking"}

# def is_valid_board(some_dictionary, list_of_figures):

#     if len(some_dictionary) <= 32: #sprawdzanie calkowitej ilosci
#         white, black = 0, 0
#         for figure in some_dictionary.values(): #loop w slowniku.values
#             if figure[0] == "w": #jezeli figura jest white
#                 white += 1
                
#                 if white > 16:
#                     print("Too many white pieces!")
#                     break
#                 else:
#                     if figure[1:] not in list_of_figures:
#                         print("Invalid figure: " + figure[1:])
#                         break


        
#         #code here
#         pass

#     else:
#         print("Length of the dictionary invalid.\nClosing the program.")


# is_valid_board(chess_dict, figures)




# def valid_chess_board(board):
#     bpieces, wpieces = 0, 0
#     pieces = ("king", "queen", "rook", "bishop", "knight", "pawn")
#     board_pieces = list(board.values())

#     for space in board:
#         if space[0] not in "12345678" or space[1] not in "abcdefgh":
#             return False

#     if board_pieces.count("bpawn") > 8 or board_pieces.count("wpawn") > 8:
#         return False    

#     if board_pieces.count("bking") != 1 or board_pieces.count("wking") != 1:
#         return False

#     for piece in board_pieces:
#         if piece[0] == "b" and piece[1:] in pieces:
#             bpieces += 1
#         elif piece[0] == "w" and piece[1:] in pieces:
#             wpieces += 1
#         else:
#             return False

#     if bpieces > 16 or wpieces > 16:
#         return False

#     return True

# chess_board = {
#     "1a": "wrook",
#     "2a": "wpawn",
#     "6a": "bpawn",
#     "8a": "brook",
#     "2b": "wpawn",
#     "5b": "bpawn",
#     "1c": "wbishop",
#     "2c": "wbishop",
#     "3c": "wpawn",
#     "6c": "bknight",
#     "7c": "bpawn",
#     "1d": "wqueen",
#     "2d": "wknight",
#     "5d": "bpawn",
#     "8d": "bqueen",
#     "6e": "bking",
#     "7e": "bbishop",
#     "1f": "wrook",
#     "2f": "wpawn",
#     "3f": "wknight",
#     "6f": "bknight",
#     "8f": "brook",
#     "1g": "wking",
#     "2g": "wpawn",
#     "7g": "bpawn",
#     "8g": "bking",
#     "2h": "wpawn",
#     "7h": "bpawn",
# }

# print(valid_chess_board(chess_board))






# # inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         # FILL THIS PART IN
#         item_total += v
#         print(v, k)
#     print("Total number of items: " + str(item_total))

# def addToInventory(inventory, addedItems):
#     # your code goes here
#     for new_item in addedItems:
#         if new_item in inventory.keys():
#             inventory[new_item] += 1
#         else:
#             inventory[new_item] = 1
#     return inventory

# # #def s_if_multiple(inventory):
# #  #   for k, v in inventory.items():
# #   #      if v > 1:
# #    #         # print(k)
# #     #        inventory[k+"s"] = inventory.pop(k)
# #      #       # print(k)
# #    # return inventory
            

    
    
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', "rope", 
#               "horse", "horse"]
# inv = addToInventory(inv, dragonLoot)
# # inv = s_if_multiple(inv)
# displayInventory(inv)



# print("ala ma"\
#     "kota")



# print("""ala
# ma
# kota""")



# sentence = "Remember, remember, the fifth of November."

# print(sentence)
# print(type(sentence))
# sentence = sentence.split()
# print(sentence)
# print(type(sentence))
# print(sentence[5][-2::-1].lower())


# rjust() ljust() center()
# lstrip() rstrip()


#DATE DETECTION


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log[0]["cities"][2])
















