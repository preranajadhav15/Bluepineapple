def split_at_lowercase(string):
    result=[]
    split=""

    for i in string:
        if i.islower():
            result.append(split)
            split=i
        else:
            split+=i

    result.append(split)
    return result
print(split_at_lowercase("pRERanA"))
