# numbers = [10, 5, 6, 2, 1]
# print(numbers)
# numbers[0] = 1111
# print(numbers)
# del  numbers[1]
# print(numbers)

# #3.4.1.6 LAB
# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
# middle_element =  (len(hat_list) -1) // 2
# hat_list[middle_element] = int(input("replace middle element: "))
# # Step 2: write a line of code that removes the last element from the list.
# del hat_list[len(hat_list)-1]
# # Step 3: write a line of code that prints the length of the existing list.
# print(len(hat_list))
# print(hat_list)

# my_list = [10, 1, 8, 3, 5]
# total = 0
# # print(len(my_list))
# for i in range(len(my_list)):
#     total += my_list[i]
#
# print(total)

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add = 0
    add += number
    lst_2.append(add)

print(lst_2)
