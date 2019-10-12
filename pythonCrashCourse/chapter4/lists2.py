# Numerical lists using loops
# for value in range(1, 5):
#     print(value)

numbers = list(range(1, 6))
print(f"Printing the numbers list: {numbers}")

# Create a list with only even numbers
evenNumbers = list(range(2, 11, 2))
print(f"Printing even numbers list: {evenNumbers}")

# Make a list of squares
squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(f"List of squares: {squares}")

squares2 = [value ** 2 for value in range(1, 11)]
print(squares2)

# Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(f"Players list: {players}")
print(players[0:3])

# Slicing using a for loop
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

# Copy a list
myFoods = ["pizza", "falafel", "carrot cake"]
friendFoods = myFoods[:]

print("My favorite foods are:")
print(myFoods)

print("\nMy friend's favorite foods are:")
print(friendFoods)

# Add items to each list to prove they're not the same object
myFoods.append("cannoli")
friendFoods.append("ice cream")

print("My favorite foods are:")
print(myFoods)

print("\nMy friend's favorite foods are:")
print(friendFoods)

# Practice problems
# players = ["charles", "martina", "michael", "florence", "eli"]
print(f"The first three items in the list are: {players[:3]}")
print(f"Three items from the middle of the list are: {players[1:4]}")
print(f"The last three items in the liast are: {players[2:]}")