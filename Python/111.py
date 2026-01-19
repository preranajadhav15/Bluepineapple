def common_elements(nested_list):
    result=[]
    for item in nested_list[0]:
        if all(item in lst for lst in nested_list[1:]):
               result.append(item)
    return result

lst=[[1,2,3],[2,3,4],[2,3,5]]
print(common_elements(lst))