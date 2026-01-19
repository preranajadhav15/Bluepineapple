import math
def complex_angle(z):
    x=z.real
    y=z.imag
    return math.degrees(math.atan2(y,x))
z1=complex(1,1)
z2=complex(1,-1)
z3=complex(-1,1)
z4=complex(-1,-1)
print(complex_angle(z1))
print(complex_angle(z2))
print(complex_angle(z3))
print(complex_angle(z4))