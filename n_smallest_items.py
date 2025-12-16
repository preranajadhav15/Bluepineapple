def n_smallest_items(data, n):
    sorted_data = sorted(data)   
    result=sorted_data[:n]
    return result
data=[4,1,9,2,3,8,11]
print(n_smallest_items(data,2))
