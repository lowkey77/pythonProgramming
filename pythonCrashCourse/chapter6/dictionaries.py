# Dictionaries
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# Adding values to a dictionary
print("\nThis is the current dictionary:")
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print("\nThis is the new dictionary after adding x and y positions")
print(alien_0)

# A dictionary of similar objects
favoriteLanguages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python"
}
person = "sarah"

print(f"\nSara's favorite language is {favoriteLanguages.get(person).title()}.")

# Looping through all key-value pairs
for key, value in favoriteLanguages.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print()

for name, language in favoriteLanguages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
print()

# print only the keys in a dictionary
for name in favoriteLanguages.keys():
    print(name.title())
print()

# print only the values in a dictionary
for value in favoriteLanguages.values():
    print(value.title())
print()
