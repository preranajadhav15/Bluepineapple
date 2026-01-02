def division_1st_even_odd(l):
    even=[]
    odd=[]

    for i in range(len(l)):
        if l[i]%2==0:
            even.append(l[i])
        else:
            odd.append(l[i])
         

    result=even[0]/odd[0]
    return result
l=[3,5,6,7]
print(division_1st_even_odd(l))
