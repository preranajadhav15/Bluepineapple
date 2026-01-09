def squares_in_retangle(num1,num2):
    count=1
    for i in range(0,min(num1,num2)):
        count+=((num1-i)*(num2-i))
    return count-1
print(squares_in_retangle(4,6))