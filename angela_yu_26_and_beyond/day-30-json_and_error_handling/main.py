# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as key_error_message:
#     print(f"the key {key_error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed.")\
#     raise TypeError("made up error")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("human height are not over 3 meters")

bmi = weight / height ** 2
print(bmi)