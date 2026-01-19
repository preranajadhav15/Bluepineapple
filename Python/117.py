def convert_to_float(lst):
    result=[]
    for i in lst:
        if type(i)==int or type(i)==float:
            result.append(float(i))
        elif type(i)==str and i.replace('.','',1).isdigit():
            result.append(float(i))
        else:
            result.append(i)
    return result
lst=[1,2,3.5,'abc','3']
print(convert_to_float(lst))