def all_num_different(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                return False
    return True

l=[1,2,3,4]
print(all_num_different(l))

