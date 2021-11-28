def paper_doll(text):
    temp_text = []
    for letter in text:
        temp_text.append(letter*3)
        # print(letter * 3)
    # print(type(temp_text))
    word = "".join(temp_text)
    # print(type(word))
    print(word)
    return word
    # print(temp_text)
paper_doll("Hello")
paper_doll("Mississippi")