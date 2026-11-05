from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Input Username --> ")
    password = getpass("Input Password --> ")

    if username == "user1" and password == "kate123" :
        print("access granted")
        isLogin = True
    else:
        print("access denied")
        