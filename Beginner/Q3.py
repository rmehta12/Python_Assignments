marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
percentage = sum(marks) / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Percentage: {percentage}% - Grade: {grade}")
