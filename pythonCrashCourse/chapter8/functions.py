# Functions
def greetUser():
    """Display a simple greeting."""
    print("Hello!")


greetUser()


def greetUser(name):
    print(f"Hello {name.title()}!")


greetUser("Reggie")


# Optional Arguments
# Set optional argument as the last one, with a default of an empty string.
def getFormattedName(firstName, lastName, middleName=""):
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"
    return fullName.title()


# print(getFormattedName("reggie", "key"))


# Returning a Dictionary
def buildPersion(firstName, lastName, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": firstName, "last": lastName}

    if age:
        person["age"] = age
    return person


# print(buildPersion("reggie", "key", str(21)))

while True:
    print("\nplease tell me your name: ")
    print("(Enter 'q' at any time to quit)")

    fName = input("First name: ")
    if fName.strip() == "q":
        break

    lName = input("Last name: ")
    if lName.strip() == "q":
        break

    formattedName = getFormattedName(fName, lName)
    print(f"\nHello, {formattedName}")
