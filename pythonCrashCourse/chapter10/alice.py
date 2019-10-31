# Handling the FileNotFoundError Exception
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file \"{filename}\" was not found.")
else:
    # Count the approximate words in the file.
    words = contents.split()
    num_words = words.__len__()
    print(f"The file {filename} has about {num_words} words.")
