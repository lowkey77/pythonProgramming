"""Write a program in Python that checks whether "Josh"
is on the list and also checks whether "Marie" is not on the list.
The list of members is "Josh, Adam, Ervin". """

personList = ["Josh", "Adam", "Ervin"]
josh = "Josh"
marie = "Marie"

print("Josh is in the list: ", josh in personList)
print("Marie is not in the list: ", marie not in personList)