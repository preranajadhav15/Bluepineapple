def tuple_frequency(tup):
    freq={}
    for i in tup:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
tup=[(1,2),(1,3),(1,2),(1,4),(1,2),(1,3)]
print(tuple_frequency(tup))