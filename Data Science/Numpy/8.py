#Missing Values Simulation


import numpy as np

#Create a 1D float array of size 40
float_arr=np.random.rand(40)
print("Float array:\n",float_arr)
print(float_arr.dtype)

#Randomly turn 20% positions into np.nan
persentage=0.2

nan_num=int(float_arr.size*persentage)
indices=np.random.choice(float_arr.size,nan_num,replace=False)
float_arr[indices]=np.nan
print(f"After randomly truning {nan_num} into nan:\n",float_arr)

#Compute mean ignoring NaNs
mean_without_nan=np.nanmean(float_arr)
print("Mean ignoring nan values: ",mean_without_nan)

#Replace NaNs with the median of non-NaN values
median_without_nan=np.nanmedian(float_arr)

#replacing using known indices
float_arr[indices]=median_without_nan
print("After replacing nan values with median of non-nan values:\n",float_arr)

#without using indices
"""
arr_filled = float_arr.copy()
arr_filled[np.isnan(arr_filled)] = median_without_nan

print("Array after replacing NaNs with median:\n", arr_filled)
"""