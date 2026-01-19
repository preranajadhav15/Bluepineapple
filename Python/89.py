def closest_smaller(lst,n):
    for i in sorted(lst,reverse=True):
        if i<n:
            return i
    return None
l=[1,23,14,56]
n=34
print(closest_smaller(l,n))