# Functions with undetermined number of parameters
def makePizza(name, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\n{name.title()} ordered a pizza with the following toppings: ")
    for topping in toppings:
        print(f"\t- {topping}")


makePizza("reggie", "pepperoni")
makePizza("reggie", "pepperoni", "ham", "bacon")


# Using arbitrary keyword arguments
def buildProfile(first, last, **userInfo):
    """Build a dictionary containing everything we know about a user."""
    userInfo["firstName"] = first
    userInfo["lastName"] = last
    return userInfo


user_profile = buildProfile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
