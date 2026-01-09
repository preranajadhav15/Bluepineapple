def check_equilateral_triangle(side1,side2,side3):
    if side1==side2 and side1==side3 and side2==side3:
        return "It is equilateral triangle"
    else:
        return "It is not equilateral triangle"
print(check_equilateral_triangle(2,3,2))