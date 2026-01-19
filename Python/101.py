def find_kth_element(arr,k):
    if k<=0 or k>len(arr):
        return "outoff range"
    return arr[k-1]
arr=[10,20,30,40]
print(find_kth_element(arr,4))