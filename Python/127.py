def multiplication_without_star_operator(num1,num2):
    result=0
    negative=False
    if (num1<0 and num2>=0) or (num1>=0 and num2<0):
        negative=True
    num1=abs(num1)
    num2=abs(num2)
    for _ in range(num2):
        result+=num1
    return -result if negative else result
print(multiplication_without_star_operator(2,3))