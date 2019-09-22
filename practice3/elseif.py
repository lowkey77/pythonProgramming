""" Write a program that calculates the percentage based on total marks
and marks obtained and checks.
If the percentage is above or equal to 90, display "A grade"
If the percentage is below 90, but above or equal to 80, display "B Grade"
Else, display "F grade"
Consider Total marks = 500 and marks obtained 450 """

totalMarks = 500
marksObtained = 450

if marksObtained / totalMarks >= 0.90:
    print("A grade")
elif 90 > marksObtained / totalMarks >= 0.80:
    print("B grade")
else:
    print("F grade")


