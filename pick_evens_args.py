def myfunc(*args):
    my_list = []
    for item in args:
        if item % 2 == 0:
            my_list.append(item)
        else:
            pass
    return my_list

# wpis = int(input("Give numbers:"))
# myfunc(wpis)