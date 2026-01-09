def max_len_subsequence(arr,difference):
    dictionary={}
    max_len=0
    for i in arr:
        if i-difference in dictionary:
            dictionary[i]=dictionary[i-difference]+1
        else:
            dictionary[i]=1
        max_len=max(max_len,dictionary[i])
    return max_len
    
arr=[1,2,3]
print(max_len_subsequence(arr,2))