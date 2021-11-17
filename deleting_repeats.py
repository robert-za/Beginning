# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# for i in my_list:
#     for j in my_list((i+1):len(my_list))
#         if i == j:
#             print("kuku")
# #
# print("The list with unique elements only:")
# print(my_list)
#
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# print(len(my_list))
# for i in my_list:
#     for j in my_list((i + 1):(len(my_list)) - 1)
#         if i == j:
#             print("kuku")
# #
# print("The list with unique elements only:")
# print(my_list)
#
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# #
# print(len(my_list))
# for i in my_list:
#     x = i + 1
#     y = len(my_list) - 1
#     for j in my_list(x:y)
#         if i == j:
#           print("kuku")
# #
# print("The list with unique elements only:")
# print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
print(len(my_list))
my_list.sort()
print(my_list)
for i in my_list:
    for j in my_list[(i + 1):(len(my_list)) - 1]:
        print(i, j)
        if i == j:
            print("HERE")
#
print("The list with unique elements only:")
print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#my_list = [1, 1, 2, 2, 2, 4, 4, 4, 6, 9]
#
#print(len(my_list))
my_list.sort()
print(my_list)
for i in my_list:
    for j in my_list[(i + 1):(len(my_list))]:
        #print(i, j, "count\n")
        if my_list[i] == my_list[j]:
            print(my_list[i], my_list[j])
            # print("HERE\n")
#
print("The list with unique elements only:")
print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#my_list = [1, 1, 2, 2, 2, 4, 4, 4, 6, 9]
#
#print(len(my_list))
my_list.sort()
print(my_list)
for i in my_list:
    for j in my_list:
        #print(i, j, "count\n")
        if my_list[i] == my_list[j]:
            #del my_list()
            print(my_list[i], my_list[j])
            # print("HERE\n")
#
print("The list with unique elements only:")
print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#my_list = [1, 1, 2, 2, 2, 4, 4, 4, 6, 9]
#
#print(len(my_list))
my_list.sort()
print(my_list)
for i in my_list:
    for j in my_list[1:len(my_list)]:
        #print(i, j, "count\n")
        if my_list[i] == my_list[j]:
            #del my_list()
            print(my_list[i])
            # print("HERE\n")
#
print("The list with unique elements only:")
print(my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#my_list = [1, 1, 2, 2, 2, 4, 4, 4, 6, 9]
#
#print(len(my_list))
tempList = []
my_list.sort()
print(my_list)
for i in my_list:
    for j in my_list[1:len(my_list)]:
        #print(i, j, "count\n")
        if my_list[i] == my_list[j]:
            if i not in tempList:
                tempList.append(i)
            #del my_list()
            #print("HERE\n")
print(tempList)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
tempList = []
for i in my_list:
    if i not in tempList:
        tempList.append(i)
print("The list with unique elements only:")
print(tempList)
