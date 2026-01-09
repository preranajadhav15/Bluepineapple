def containing_sublist(arr,sub_arr):
    n=len(arr)
    m=len(sub_arr)
    if m==0:
        return True
    for i in range(n-m+1):
        if(arr[i:i+m]==sub_arr):
            return True
    return False
    
arr=[1,2,3,4,5,6]
sub_arr=[1,2,3]
print(containing_sublist(arr,sub_arr))