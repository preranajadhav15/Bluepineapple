def sum_common_divisor(num1,num2):
    total=0
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            total+=i
    return total
print(sum_common_divisor(6,12))
print(sum_common_divisor(13,26))
print(sum_common_divisor(24,56))