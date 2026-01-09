def counting_sort(arr):
    if len(arr)<=1:
        return arr
    maximum=max(arr)
    count=[0]*(maximum+1)
    for i in arr:
        count[i]+=1
    
    k=0
    for i in range(len(count)):
        while count[i]>0:
            arr[k]=i
            k+=1
            count[i]-=1
    return arr

arr=[0,1,7,6,3,9,6,4,7,2]
print(counting_sort(arr))






    
    