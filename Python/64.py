def sort_tuple(lists):
    result=sorted(lists,key=lambda x: (x[0],x[1]))
    return result

lists=[[1,2],[2,3],[1,1],[1,3]]
print(sort_tuple(lists))