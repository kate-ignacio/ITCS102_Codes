drinks = ["water", "alcohol", "juice", "milk", "lemonade"]

#dictionary
#key, value
drinks_d = {"mapait":"alcohol", "maasim":"leamonade", "bland":"water", "sweet":"juice", "masarap":"juice"}

print(drinks[6])
print(drinks_d["okay lang naman"])

#traveling a dictionary

for x, y in drinks_d.items():
    print("key is",x,"-- value is", y)