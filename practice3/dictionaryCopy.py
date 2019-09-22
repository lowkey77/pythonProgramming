#  Exchange the contents of two dictionaries

dictionaryA = {"A": "Apple", "B": "Ball", "C": "Cat"}
dictionaryB = {"A": "Ant", "B": "Basket", "C": "Carrot"}

intermediateDictionary = {}

print("Output of current dictionaries: ")
print("Dictionary A: ", dictionaryA)
print("Dictionary B: ", dictionaryB)

print("Exchanging values between dictionaries")

intermediateDictionary = dictionaryA
dictionaryA = dictionaryB
dictionaryB = intermediateDictionary

print()
print("Output of current dictionaries: ")
print("Dictionary A: ", dictionaryA)
print("Dictionary B: ", dictionaryB)