alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
# def encrypt(text_fun, shift_fun):

#   encrypted_word = ""
#   for letter in text_fun:
#     if letter != " ":
#       encrypted_index = alphabet.index(letter) + shift_fun
#       if encrypted_index > 25:
#         encrypted_index %= 26
#       encrypted_word += alphabet[encrypted_index]
#     else:
#       encrypted_word += " "
#   print(f"The encoded text is {encrypted_word}.")

# def decrypt(text_fun, shift_fun):
#     decrypted_word = ""
#     for letter in text_fun:
#       if letter != " ":
#         decrypted_index = alphabet.index(letter) - shift_fun
#         if decrypted_index < 0:
#             decrypted_index %= 26 * (-1)
#         decrypted_word += alphabet[decrypted_index]
#       else:
#         decrypted_word += " "
#     print(f"The decoded text is {decrypted_word}.")

def caesar(text_fun, shift_fun, direction_fun):
  message = ""
  for letter in text_fun:
    if letter in alphabet:
      if direction_fun == "encode":
        encrypted_index = alphabet.index(letter) + shift_fun
        if encrypted_index > 25:
          encrypted_index %= 26
      elif direction_fun == "decode":
        encrypted_index = alphabet.index(letter) - shift_fun
        if encrypted_index < 0:
            encrypted_index %= 26 * (-1)
      message += alphabet[encrypted_index]
    else:
      message += letter
  print(f"The {direction}d text is {message}.")


# if direction.lower() == "encode":
#     encrypt(text, shift)
# elif direction.lower() == "decode":
#     decrypt(text, shift)
# else:
#     print("wrong")
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)
  is_going = input("Continue? Yes or Not\n")
  if is_going == "no":
    break
  elif is_going == "yes":
    continue