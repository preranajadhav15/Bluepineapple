def first_duplicate(arr):
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return(arr[i])
            
arr=[1,2,2,3,4,4]
print(first_duplicate(arr))
