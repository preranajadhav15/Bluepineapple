def divisors(num):
    if num<=0:
        return 0
    div=[]
    for i in range(1,num+1):
        if num%i==0:
            div.append(i)
    return div
print(divisors(-24))
print(divisors(14))