# Get amount from user
amount = int(input("Enter amount of money: "))
original = amount

# Denominations — largest to smallest, separated 1000 and 500
p1000 = amount // 1000
amount = amount % 1000

p500 = amount // 500
amount = amount % 500

p200 = amount // 200
amount = amount % 200

p150 = amount // 150
amount = amount % 150

p20 = amount // 20
amount = amount % 20

p10 = amount // 10
amount = amount % 10

p5 = amount // 5
amount = amount % 5

p1 = amount // 1


print("Amount Entered:", original)
print("1000 :", p1000)
print("500  :", p500)
print("200  :", p200)
print("150  :", p150)
print("20   :", p20)
print("10   :", p10)
print("5    :", p5)
print("1    :", p1)
