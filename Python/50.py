def minimum_length_list(lists):
    # result=min(lists,key=lambda x:len(x))
    result=list(filter(lambda x:len(x)==min(map(len,lists)),lists))
    return result

lists=[[1,2,3,4],[1,2],[1,2,3],[2],[1]]
print(minimum_length_list(lists))



