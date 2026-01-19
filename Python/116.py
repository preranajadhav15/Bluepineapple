def tuple_to_integer(tup):
    num=0
    for i in tup:
        if i<=0:
            return "All number should be positive"
        else:
            num=num*(10**len(str(i)))+i
    return num

print(tuple_to_integer((1,2,3)))
print(tuple_to_integer((1,2,-3)))