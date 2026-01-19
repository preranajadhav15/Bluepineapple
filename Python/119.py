def unique_array_elements(arr):
    arr.sort()
    n=len(arr)
    if n==0:
        return None
    unique_element=[]
    for i in range(n):
        if i==0 and arr[i]!=arr[i+1]:
            unique_element.append(arr[i])
        elif i==n-1 and arr[i]!=arr[i-1]:
            unique_element.append(arr[i])
        elif i!=0 and i!=n-1 and arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
            unique_element.append(arr[i])
    return unique_element

arr=[1,1,1,2,3,4,3,2,5,6]
print(unique_array_elements(arr))