def recursion_sum(lists,length=0):
    if length==len(lists):
        return 0
    return lists[length]+recursion_sum(lists,length+1)
lists=[1,4,2,6,8]
print(recursion_sum(lists))