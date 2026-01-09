def tuples_length_equal(arr):
    if not arr:
        return True
    length=len(arr[0])
    for i in arr:
        if len(i)!=length:
            return False
    return True
arr=[[1,2],[2,3],[1,3]]
print(tuples_length_equal(arr))