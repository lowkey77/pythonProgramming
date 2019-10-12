# This is practice using Lists in Python

# Declare a list with different types
myList = ["Beginner to expert", 0, 1, "and", 3.142]

# Print the list
#print(myList)

bicycles = ["trek", "cannondale", "redline", "specialized"]
motorcycles = ["honda", "yamaha", "suzuki"]

# Print list bicycles
print(f"Print bicycle list: {bicycles}")

# Print first element in list
print(f"Printing first element in bicycle list: {bicycles[0]}")

# Print first element in list with title formatting
print(f"Printing first element with title casing: {bicycles[0].title()}")

# Print the last item in the list
print(f"Print the last item in the list: {bicycles[-1]}\n")

# Print motorcycles list
print(f"Initial motorcycles list: {motorcycles}")
# Change the first item of the motorcycles[] list
motorcycles[0] = "ducati"
print(f"Motorcycles list after changing first element: {motorcycles}")
motorcycles[0] = "honda"

# Append ducati to the end of the list
motorcycles.append("ducati")
print(f"Motorcycles list after appending ducati: {motorcycles}")

# Inserting an item into a list
motorcycles.insert(0, "ducati")
print(f"Print list after insert: {motorcycles}")

# Delete an item from a list
del motorcycles[-1]
print(f"List after deleting last item: {motorcycles}")

# Pop an item from the list
poppedListItem = motorcycles.pop()
print(f"Item being popped from the list: {poppedListItem.title()}")
print(f"List after popped item: {motorcycles}")

# Select item to pop from the list
selectedItem = motorcycles.pop(1)
print(f"Item being popped from the list: {selectedItem.title()}")
print(f"List after popped item: {motorcycles}")

# reinitialize list
motorcycles = ["honda", "yamaha", "suzuki"]

# Another way to remove an item from the list
motorcycles.remove("yamaha")
print(f"List after removing yamaha: {motorcycles}\n")

# Create cars list
cars = ["bmw", "audi", "toyota", "subaru"]

# Sort list alphabetically
cars.sort()
print(f"Sorted cars list: {cars}")

# Reverse sort of list
cars.sort(reverse=True)
print(f"Reversed cars list: {cars}")

# Create cars list
cars = ["bmw", "audi", "toyota", "subaru"]

#temporary sorted list
print(f"Temporarily sorted list: {sorted(cars)}")
print(f"Temporarily reverse sorted list: {sorted(cars)}")
print(f"Print same object without sort: {cars}")

# reverse the ilst
cars.reverse()
print(f"Reverse the cars list: {cars}")
print(f"The length of the list is: {cars.__len__()}")