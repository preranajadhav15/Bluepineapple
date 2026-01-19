def frequency_of_lists(lst):
    frequency={}
    for i in lst:
        tup=tuple(i)
        if tup in frequency:
            frequency[tup]+=1
        else:
            frequency[tup]=1
    return frequency
lst=[[1,2],[12,12],[1,2],[3,2],[1,2]]
print(frequency_of_lists(lst))