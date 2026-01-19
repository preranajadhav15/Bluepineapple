def sort_sublist(lst):
    return list(map(lambda x: sorted(x),lst ))
lst=[['c','a','b'],['m','q','e'],['w','d','p']]
print(sort_sublist(lst))