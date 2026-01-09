import heapq
from collections import Counter

def top_k_elements(num,k):
    count=Counter(num)
    arr=[]
    for i,j in count.items():
        heapq.heappush(arr,(j,i))
        if len(arr)>k:
            heapq.heappop(arr)
    result=[]
    for i in arr:
        result.append(i[1])
    result.sort(key=count.get, reverse=True)  
    return result
num=[1,1,1,1,1,2,3,4,4,5]
print(top_k_elements(num,2))
    
    