# with open("operations.txt") as file:
#     contents = file.read()
#     print(contents)

with open("operations.txt", mode = "a") as file:
    file.write("\nAdded line.")