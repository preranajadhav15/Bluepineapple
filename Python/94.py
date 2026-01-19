def extract_min_index_record(tup,index):
    min_value=tup[0][index]
    position=0
    for i in range(1,len(tup)):
        if tup[i][index]<min_value:
            min_value=tup[i][index]
            position=i
    return position,tup[position]

tup1=[(1,2),(3,9),(4,5),(3,1)]
tup2=[(1,2),(3,6),(4,5),(3,4)]
print(extract_min_index_record(tup1,1))
print(extract_min_index_record(tup2,0))