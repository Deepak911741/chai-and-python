# score = 85
score = int(input("Enter your marks : "))

if score >= 101:
    print("Plese verify your garde again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 80:
    grade = "C"
elif score >= 70:
    grade = "D"
else:
    grade = "F"
    
print("Grade : ", grade)