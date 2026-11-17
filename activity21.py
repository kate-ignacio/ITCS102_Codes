# fruit 1 = longgan
# fruit 2 = lansones
# fruit 3 = apple
# fruit 4 = star apple
# fruit 5 = duhat
# fruit 6 = mangosteen

fruits = [] #list , an empty list

fruits = ["longgan", "lansones", "apple"]
print(fruits)
fruits.append("star apple")
fruits.append("duhat")
print(fruits)
fruits.append("mangosteen")
fruits.append("apple")
fruits.append("lansones")

#index -- address, ZERO
print(fruits[0])
print(fruits[3])
#list slicing
print(fruits[0:3])