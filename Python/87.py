def merge_dictionary(dict1,dict2,dict3):
    return dict1 | dict2 | dict3
d1={'a':1,'b':2}
d2={'c':3}
d3={'d':4,'e':5}
print(merge_dictionary(d1,d2,d3))