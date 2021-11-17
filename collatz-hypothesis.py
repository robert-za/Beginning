c0 = int(input("pick a number"))
counter = 0
if c0 > 0:
    while c0 != 1:
        if c0%2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 +1
        counter += 1
        print(c0)
    print("Steps = ",counter)
else:
    print("Wrong number")
