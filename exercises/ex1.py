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

import random
numberOfStreaks = 0
streak = 0
my_list = []
test = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    my_list = []
    for i in range(100):
        my_list.append(random.randint(0,1))


    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(len(my_list)):
        if j == 0:
            pass
        elif my_list[j] == my_list[j-1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1
            streak = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))





































    









































