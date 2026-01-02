def nth_proper_factor(num1,num2,n):
    if num1 >= num2:
        print("Not proper factor")


    fraction=num1/num2
    fraction=fraction*(10**n)
    digit=int(fraction)%10
    return digit


print(nth_proper_factor(1,7,3))
