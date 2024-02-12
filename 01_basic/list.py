chai = ["Green", "white", "Black", "Cofy"]
print(chai)
print(chai[0])
print(chai[-1]) # Last Value
print(chai[1:3]) # Slicing
print(chai[:3]) # Slicing
print(chai[0:]) # Slicing


chai[2] = "Masala Tea"
print(chai)


chai[1:2] = ["Masala Tea"] # slicing value add

chai[1:1] = ["test", "test"]


# chai[1:1] = [] #empty aaray


for tea in chai:
    print(tea, end="-")


chai.append("chaska chai")  # append ka kam hota hai ki list ke antem me ja ke usko add kar deta hai
chai.pop("chaska chai")  # pop ka kam hota hai ki list ke antem me ja ke usko remove kar deta hai


chai.remove("green") # iska use remove ke lite karte hai

chai.insert(1, "green") # ye value ko add karta hai

tea_varity = chai.copy() # -> refrnces alag karne ke liye copy ka use karte hai


tea_varity.append("Lemon")
print(tea_varity)

print(chai)


range(0, 10)
print(range(10))



sque = [x**2 for x in range(10)]
print(sque)


cube = [y**3 for y in range(5)]
print(cube)
 