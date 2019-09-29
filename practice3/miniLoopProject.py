# Input variables
startNumber = 13
stopNumber = 4

#Even and odd counter integers
evenCounter = 0
oddCounter = 0

if startNumber < stopNumber:
    for x in range(startNumber, stopNumber, 1):
        print(x)
        if x % 2 == 0:
            evenCounter += 1
        else:
            oddCounter += 1
elif startNumber > stopNumber:
    for x in range(startNumber, stopNumber, -1):
        print(x)
        if x % 2 == 0:
            evenCounter += 1
        else:
            oddCounter += 1
else:
    print("The values are equal")
# Print counts of even and odd
print("Even counter: ", evenCounter)
print("Odd counter: ", oddCounter)