# Fancy Indexing  Scatter Update
    
import numpy as np

#Create a length-30 zero array.
arr=np.zeros(30)
print(f"Array:\n {arr}")
 
#Randomly pick 8 unique positions and set them to 1.
unique_indices=np.random.choice(30,size=8,replace=False)
arr[unique_indices]=1

print("Array after setting the 8 unique position as 1:\n",arr)

#Then set positions divisible by 5 to 9 (overwriting if needed).
arr[::5]=9
print("Ater setting the position divisible by 5 to 9:",arr)