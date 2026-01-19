def maximum_frequency(lst: list) -> int:
    freq={}
    max_count=0
    result=[]
    for i in lst:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for count in freq.values():
        if count>max_count:
            max_count=count
    for i in freq:
        if freq[i]==max_count:
            result.append(i)
    return result

if __name__ == "__main__":
    lst=[1,2,1,2,3,4,4]
    print(maximum_frequency(lst))


