def smallest_number(arr):
    smallest=arr[0]
    for i in range(1,len(arr)):
        if smallest>arr[i]:
            smallest,arr[i]=arr[i],smallest
    return smallest
l=[3,2,1,6,5]
print(smallest_number(l))