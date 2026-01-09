def is_monotonic(arr):
    if len(arr)<=2:
        return True
    monotonical_increasing=True
    monotonical_decrasing=True
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            monotonical_decrasing=False
        elif arr[i]<arr[i-1]:
            monotonical_increasing=False
    return monotonical_increasing or monotonical_decrasing

arr=[1,2,3]
print(is_monotonic(arr))