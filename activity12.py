import getpass

username = 'kate123'
password = 'kate111'

u = input("Enter Username ---> ")
p = getpass.getpass("Enter Password ---> ")

if username == u and password == p :
      print("ACCESS GRANTED")
else: 
      print("ACCESS DENIED")