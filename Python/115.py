def is_empty_dict(dict_list):
    for i in dict_list:
        if i:
            return False
    return True
dict_list1=[{},{}]
dict_list2=[{1:2},{}]
dict_list3=[{1:2},{2:3}]
print(is_empty_dict(dict_list1))
print(is_empty_dict(dict_list2))
print(is_empty_dict(dict_list3))