def multiples_of_number(m,n):
    multiple=[]

    for i in range(1,m+1):
        multiple.append(i*n)
    return multiple
print(multiples_of_number(3,4))
