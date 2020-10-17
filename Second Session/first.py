grade = int(input("Enter your grade: "))
letter_grade = ""


if grade < 60:
	letter_grade = "F"
elif grade < 70:
	letter_grade = "D"
elif grade < 80:
	letter_grade = "C"
elif grade < 90:
	letter_grade = "B"
else:
	letter_grade = "A"

print("Your grade is: " + letter_grade)
