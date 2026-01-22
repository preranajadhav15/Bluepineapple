import numpy as np

arr=np.arange(1,21)
print("Array:", arr)

print(f"Shape:",arr.shape)
print("Data Type:",arr.dtype)
print("Minimum:",arr.min())
print("Maximum:",arr.max())
print("Total:",arr.sum())
print("Mean:",arr.mean())

float_arr=arr.astype(float)
print("Float Array:",float_arr)
print("Data type after conversion:",float_arr.dtype)
