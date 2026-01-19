from collections import Counter
def list_elements_frequency(lst):
    frequency=Counter(lst)
    return frequency
l=[1,1,2,3,2,2,4,3]
print(list_elements_frequency(l))