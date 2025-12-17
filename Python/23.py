def max_sum_row(lists):
    rows=len(lists)

    for i in range(rows):
        for j in range(i+1,rows):
            if sum(lists[i]) > sum(lists[j]):
                lists[i], lists[j] = lists[j], lists[i]
    return lists[i]


lists=[[2,4,4],[6,2,3],[1,1,1]]
print(max_sum_row(lists))
