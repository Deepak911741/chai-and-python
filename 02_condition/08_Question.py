password = "Secure@123456"

if len(password) < 6:
    char = "Weak"
elif len(password) <= 10:
    char = "Medium"
elif len(password) > 10:
    char = "Strong"
else:
    print("No Data")
    
print(char)
print(len(password))