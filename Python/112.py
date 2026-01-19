import math

def perimeter_of_cylinder(radius):
    if radius<=0:
        return 0
    return 2*math.pi*radius
print(perimeter_of_cylinder(2))
print(perimeter_of_cylinder(-2))