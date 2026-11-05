for x in range(5):
    for y in range(5):
        if x+y == 4 or y==x:
            print("*", end ="")
        else:
            print(" ", end ="")
    print()