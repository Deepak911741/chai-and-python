username = "Deepak kumar"

def func(): #->esko pythone ne scope kahte hai dusre languge me ese {} es tarh se likte hai
    username = "Deepak"
    print(username)
    
print(username)
func()


x = 99
def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)