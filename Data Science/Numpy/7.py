#Sorting  Top-K Without Full Sort

import numpy as np

#Create 100 random numbers (floats)
float_arr = np.random.rand(100)   
print("Float array:\n",float_arr)

#Find top 10 values and their indices using an efficient approach (argpartition)

N = 10

#partitioning array in top 10 largest value at the end and remaining value at begnning
top_10_indices=np.argpartition(float_arr,-N)[-N:]
print("TOp 10 indices:\n",top_10_indices)

top_10_values = float_arr[top_10_indices]
print('Top 10 values:\n',top_10_values)

#Print top 10 sorted descending (values + indices aligned)

#reversing the order (decending)
order = np.argsort(top_10_values)[::-1]

#sorting top 10 values using order
sorted_top_10_values = top_10_values[order]

#sorting aligned indices 
aligned_top_10_indices = top_10_indices[order]

print("Sorted top 10 values:\n",sorted_top_10_values)
print("Aligned indices of sorted top 10 values:\n",aligned_top_10_indices)