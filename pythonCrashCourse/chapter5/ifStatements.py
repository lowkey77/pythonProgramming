# If statements
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Checking if a value is in a list
requestedToppings = ["mushrooms", "onions", "pineapple"]
topping = "mushrooms"
test = topping in requestedToppings
print(test)

# Check if value is not in a list
bannedUsers = ["andrew", "carolina", "david"]
user = "marie"

if user not in bannedUsers:
    print(f"{user.title()} is not banned.")
