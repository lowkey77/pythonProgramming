with open("../textFiles/pi_digits.txt") as file_object:
    lines = file_object.readlines()

    output = ""
    for line in lines:
        output += line.strip()

    print(output)
