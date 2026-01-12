def divisible_tuple(tup_list,k):
    result=[]
    for i in tup_list:
        if all(j%k==0 for j in i):
            result.append(i)
    return result

tup_list=[(2,4),(3,6),(4,8)]
k=2
print(divisible_tuple(tup_list,k))




