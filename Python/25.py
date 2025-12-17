def product(arr):
    multi=1

    for i in arr:
        if arr.count(i)==1:
            multi*=i
    return multi

arr=[1,2,2,4,5]
print(product(arr))
        
