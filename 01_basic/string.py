chai = "   Masala Chai   "
# stript ka use space hatane ke liye karte hai
print(chai.strip())
print(chai.replace("Masala", "Lemon"))

# Replace ka use word ko change karne ke liye karte hai


chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))


#find 

chai = "Masala Chai"
print(chai.find("Chai"))

# Ager hmare me word nhi hai to find kiya hua output -1 aaeyega

chai_type = "Masala"
quantity = 2
order = "I order {} cups of {} chai"

# {} -> eska use use ham python me variable dene ke liye karte hai 

print(order.format(quantity, chai_type))


chai_varity = ["Lemon", "masala", "Ginger"]
print("".join(chai_varity))
print(" ".join(chai_varity))
print("-".join(chai_varity))
print(", ".join(chai_varity))


chai = "Deepak kumar"
for letter in chai:
    print(letter)