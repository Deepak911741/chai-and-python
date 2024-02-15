distance = 5

if distance < 3:
    tranport = "walk"
elif distance <= 15:
    tranport = "Bike"
else:
    tranport = "Car"
    
print("AI recoments you the transport of: ", tranport)