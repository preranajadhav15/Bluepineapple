def add_list_to_tuple(lst,tup):
    return [i+(lst,) for i in tup]
lst=[1,2,3]
tup=[(4,5,6),(2,3)]
print(add_list_to_tuple(lst,tup))
