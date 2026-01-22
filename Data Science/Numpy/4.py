import numpy as np
arr=np.random.rand(4,5)
print("Array:",arr)

vector=np.random.rand(5)
print("Vector:",vector)

broadcast_sum=arr+vector
print("Afterbroadcasting addition:",broadcast_sum)

row_sum=broadcast_sum.sum(axis=1,keepdims=True)
normalized=broadcast_sum/row_sum
print("Row normalized:",normalized)

print(normalized.sum(axis=1))