def check_elements(tuple_list, k_elements):
    count = 0
    count1 = 0

    for i in k_elements:
        for j in tuple_list:
            if i == j:
                count += 1
        count1 += k_elements.count(i)

    if count == count1:
        return True
    else:
        return False
t1 = [(1,2),(2,3),(4,5)]
t2 = [(1,2),(4,5)]

print(check_elements(t1, t2))
