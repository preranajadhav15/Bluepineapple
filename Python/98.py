def multiply_and_divide(lst):
    if not lst:
        return 0
    product=1
    for i in lst:
        product*=i
    return product//len(lst)
lst1=[1,2,3,4]
lst2=[1,-2,3,4]
print(multiply_and_divide(lst1))
print(multiply_and_divide(lst2))