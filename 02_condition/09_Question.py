year =  int(input("Enter the year: "))


if (year % 100 == 0) or (year %  4 == 0 and year % 100 != 0):
    print(year, "Is a leap year")
else:
    print(year, "is not a leap year")