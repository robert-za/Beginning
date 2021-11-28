def myfunc(word):
    mod_word = []
    for i in range(len(word)):
        if i % 2 == 0:
            mod_word.append(word[i].lower())
        else:
            mod_word.append(word[i].upper())
    print("".join(mod_word))
    return ''.join(mod_word)

word = "polskakrulempolski"
myfunc(word)