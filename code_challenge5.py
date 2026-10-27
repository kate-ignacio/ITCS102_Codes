n = int(input("input size of x "))
for x in range (n):
    for y in range (n):
        if x + y == n - 1 or y==x :
            print("*", end="")
        else:
            print(" ", end="")
    print()
   
       


