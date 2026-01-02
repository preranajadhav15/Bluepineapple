def filter_even_number(l):
    return list(filter(lambda x:x%2==0,l))
l=[1,1,2,3,3,4,4]
print(filter_even_number(l))
