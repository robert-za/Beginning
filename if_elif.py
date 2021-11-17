# # OPERATORS
# # <, >, =>, =<, ==, !=
#
# # IF STATEMENT
# age = int(input('Tell me your age: '))
#
# if age < 10:
#     print('Your are young, strange one')
#     # any additional code for the block is tab-indented
# elif age < 40:
#     print('The fire in you is strong, strange one')
# else:
#     print('You are wise beyond doubt, strange one')
#
# meaty = input('Do you eat meat? (y/n): ')
#
# if meaty == 'y':
#     print('here is the meaty menu...')
# else:
#     print('here is the veggie menu...')

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
#
# del list_1[0]
# del list_2
#
# print(list_3)

# my_list = [1, 2, "in", True, "ABC"]
#
# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False
# 3.7.1.1
#
# 3.7.1.4
# temps = [[0.0 for h in range(24)] for d in range(31)]
# # for d in range(31):
# #     print(temps[d])
# total = 0.0
# for day in temps:
#     total += day[11]
# average = total / 31
# print("Average temperature at noon:", average)

# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x *= elem
# print(x)

# x = 1
# x = x == x
# print(x)

# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# t = [[3-i for i in range(3)] for j in range(3)]
# print(t)
# s=0
# for i in range(3):
#     s+=t[i][i]
# print(s)

# my_list = [1,2,3]
# for v in range(len(my_list)):
#     print(len(my_list))
#     print(my_list[v])
#     my_list.insert(1,my_list[v])
# print(my_list)

# var = 1
# while var < 10:
#     print("c")
#     var = var << 1
#     print(var)

i = 0
# while i <= 5:
#     i += 1
if i % 2 == 0:
        print(i%2 ==0)
print("*")
