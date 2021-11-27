# # FOR LOOPS
# # for loops can iterate over data within lists
# ninjas = ['ryu', 'crystal', 'yoshi', 'ken']
#
# for ninja in ninjas:
#     print(ninja)
#
# # can give for loops a range using slicing
# print('-----')
# for ninja in ninjas[1:7]:
#     print(ninja)

# # add additional logic to for loops
# print('-----')
# for ninja in ninjas:
#     if ninja == 'yoshi':
#         print(f'{ninja} - black belt')
#         break
#     else:
#         print(ninja)
# print(b'Easy \xE2\x9C\x85'.decode("utf-8"))
#test github

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# age = 25
# num = 0
#
# while num < age:
#     if num % 2 == 0:
#         print(num)
#     num += 1
