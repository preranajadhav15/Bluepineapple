def opposite_or_not(num1,num2):
    if( num1>=0 and num2<0) or (num1<0 and num2>=0):
        return True
    else:
        return False
    
print(opposite_or_not(1,2))