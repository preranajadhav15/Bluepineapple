def n_smallest_items(data, n):
    sorted_data = sorted(set(data))   
    result=sorted_data[:n]
    return result
data=[1,2,2,2,2,2,2]
print(n_smallest_items(data,4))
