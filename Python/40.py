from collections import defaultdict

def frequency_of_element(lists):
    count=defaultdict(int)
    for i in lists:
        for j in i:
            count[j]+=1
    return dict(count)
lists=[[1,2,3],[2,3,4],[1,3,4],[5,5,5]]
print(frequency_of_element(lists))
















    
    