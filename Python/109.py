def count_odd_rotation(binary_str):
    length=len(binary_str)
    count=0
    for i in range(length):
        rotated=binary_str[i:]+binary_str[:i]
        if rotated[-1]=='1':
            count+=1
    return count
print(count_odd_rotation("0110101"))