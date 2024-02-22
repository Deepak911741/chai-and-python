user = input("Enter a value: ")

rever_string = " "
for char in user:
    rever_string = char + rever_string
    
    if user  == rever_string:
        print("The string is palindrom")
    else:
        print("This string is not palindom")