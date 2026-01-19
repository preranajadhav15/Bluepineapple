def min_sublist(lst):
    return min(len(sub) for sub in lst)
lst=[[1,2,3],[2,3],[3],[1,2,3,4]]
print(min_sublist(lst))