import math

def circle_stats(radius):
   area =  math.pi * radius ** radius
   confrnce = 2 * math.pi * radius
   return area, confrnce
# print("hi")

a, c = circle_stats(3)
print("Area: ", a, "confrnce: ", c)