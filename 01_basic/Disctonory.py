# {} -> ye hmara Dict hai

chai_types = {"Masala": "Spicy", "Ginger":"Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types[Masala])

print(chai_types.get[Ginger])

chai_types["Green"] = "Fresh"

print(chai_types)


for chai in chai_types:
    print(chai)
    
    
for key, value in chai_types.items():
    print(key, value)
    
    
    
sqafreed_num = {x:x**2 for x in range(6)}
print(sqafreed_num)
 
 
print(sqafreed_num.clear)

keys = ["Masala", "Ginger", "Lemon"]
print(keys)


defalut_value = "Delicious"
new_dict = dic.fromkeys(keys, defalut_value)

print(new_dict)