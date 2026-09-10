# Global Freight Calculator


sender_name = input("Enter Sender Name: ")
type_of_item = input("Enter Type of Item: ")
isFragile = input("Is it Fragile? (True/False): ") == "True"
weight = float(input("Enter Weight in kg: "))
distance = float(input("Enter Distance in km: "))
is_express = input("Is Express? (True/False): ") == "True"
is_international = input("Is International? (True/False): ") == "True"

# Step 1: Calculate Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

# Step 2: Apply Rules 
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00

elif is_international and is_express:
    total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
    total = base_cost + 30

else:
    total = base_cost


print("--- SHIPPING COST ---")
print("Sender:", sender_name)
print("Base Cost:", base_cost)
print("TOTAL COST: $", total)