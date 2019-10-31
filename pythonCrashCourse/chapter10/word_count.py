# Method to handle counting words.
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file \"{filename}\" was not found.")
        pass
    else:
        # Count the approximate words in the file.
        words = contents.split()
        num_words = words.__len__()
        print(f"The file {filename} has about {num_words} words.")


filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    count_words(filename)

