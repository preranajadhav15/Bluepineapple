def area_of_paralellogram(height,base):
    if height<=0 or base<=0:
        return "Invalid input"   
    area=height*base
    return area
print(area_of_paralellogram(4,5))