def missing_number(arr):
    length=len(arr)+1
    arthimatic_sum=(arr[0]+arr[-1])*length//2
    total_sum=sum(arr)
    missing=arthimatic_sum - total_sum
    if missing in arr:
        return None
    return missing
arr=[1,2,3,5]
print(missing_number(arr))