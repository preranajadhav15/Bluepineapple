def gcd_of_two_number(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1

def gcd_of_array_number(l):
    result=l[0]
    for i in range(1, len(l)):
        result=gcd_of_two_number(result,l[i])
    return result

l=[12,3456,144]
print(gcd_of_array_number(l))


