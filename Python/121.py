def triple_sum(arr,target):
    n=len(arr)
    triplet=[]
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==target:
                    triplet.append((arr[i],arr[j],arr[k]))
    return triplet
lst=[1,2,3,4,5,6,7,8,9,0]
print(triple_sum(lst,9))