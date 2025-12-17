import math
base1=int(input("Enter the number:"))
base2=int(input("Enter the number:"))
base3=int(input("Enter the number:"))
height=int(input("Enter the number:"))
volume_of_triangularPrism=height*math.sqrt(-base1**4+2*(base1*base2)**2-base2**4+2*(base2*base3)**2-base3**4)/4
print(volume_of_triangularPrism)

