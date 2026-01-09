def comb_sort(arr):
    arr_length=len(arr)
    gap=arr_length
    shrink_factor=1.3
    
    while gap>1:
        if gap<1:
            gap=1
        gap=int(gap/shrink_factor)
        for i in range (arr_length-gap):
            if arr[i]>arr[i+gap]:
                arr[i],arr[i+gap]=arr[i+gap],arr[i]
    return arr
arr=[4,1,-3,9,6]
print(comb_sort(arr))