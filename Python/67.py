from math import comb
def count_partition_bell_number(size,dictionary={}):
    if size==0:
        return 1
    if size in dictionary:
        return dictionary[size]
    total=0
    for i in range(size):
        total+=comb(size-1,i)*count_partition_bell_number(i,dictionary)
    dictionary[size]=total
    return total
    
size=3
print(count_partition_bell_number(size))