def last_digit(num1,num2):
    if num1>num2:
        return "Invalid"
    result=1
    for i in range(num1+1,num2+1):
        result*=i
    return result%10
print(last_digit(3,10))
    