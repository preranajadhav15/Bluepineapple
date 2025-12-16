t1=([1,2],[2,3],[3,4],[4,5])
t2=([2,3],[3,4],[6,7])

def similar_elements(t1, t2):
    similar = []
    for i in t1:
        if i in t2:
            similar.append(i)
    return similar
print(similar_elements(t1,t2))
