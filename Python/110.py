def missing_number(lst,start,end):
    number=[]
    previous=start-1
    for num in lst:
        if num>previous+1:
            number.append((previous+1,num-1))
        previous=num
    if previous<end:
            number.append((previous+1,end))
    return number

lst=[1,2,4,6,8,10]
start=2
end=8
print(missing_number(lst,start,end))