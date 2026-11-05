isExpensive = True

while isExpensive == True:
    x= bool(input("is the gas price still expensive? (True/False)"))

    if x == True:
        print("Continuing Loop")
        continue
    else:
        break