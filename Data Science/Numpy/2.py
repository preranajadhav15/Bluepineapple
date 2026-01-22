import numpy as np

arr=np.random.randint(1,101,size=50)
print("Array:" , arr)

even_number = arr[arr % 2 == 0]
print("Array of even number:" , even_number)

divible3_greater50 = arr[(arr % 3 == 0) & (arr > 50)]
print("Array of numbers divisible by 3 and > 50:" , divible3_greater50)

arr[arr<20]=20
print("Replace values < 20 with 20:", arr)