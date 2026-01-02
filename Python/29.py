def odd_occurance(l):
    count=0
    result=[]
    for i in l:
    
        if l.count(i)%2!=0:
            result.append(i)
        final_output=set(result)
    return final_output
l=[1,1,1,2,2,3,3,4,4,4,5]
print(odd_occurance(l))
        
