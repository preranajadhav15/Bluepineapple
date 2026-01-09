def repeated_element_sum(l):
    add=0
    visited=[]
    for i in l:
        if l.count(i)>1 and i not in visited:
            add+=i
            visited.append(i)
    return add
l=[1,1,2,3,4,4,3,5,5]
print(repeated_element_sum(l))