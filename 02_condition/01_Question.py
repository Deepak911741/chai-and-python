# age = int(input("Enter Your Age: "))
#     # print("Your age is :", age)


age = int(input("Enter your age : "))

if age < 13:
    print("Child")
elif age < 19:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")