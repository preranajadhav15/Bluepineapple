def positive_number(l):
    count=0
    for i in l:
        if i > 0:
            count+=1
    return count
l=[-1,2,-3,4,5]
print(positive_number(l))