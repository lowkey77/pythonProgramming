# User input and loops
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nenter 'quit' to end the program. "
message = ""

while message != "quit":
    message = input(prompt).strip()
    if message != 'quit':
        print(message)

