import numpy as np

arr=np.arange(1,61).reshape(5,12)
print("Array:", arr)

row_sum=arr.sum(axis=1)
print("Row wise sum:",row_sum)

column_mean=arr.mean(axis=0)
print("Column wise mean:",column_mean)

global_std=arr.std()
print("Global standard deviation:",global_std)

max_value=arr.argmax()
row,col=np.unravel_index(max_value,arr.shape)
print(f"The maximum value is  {arr[row,col]} at index: ({row},{col})")
