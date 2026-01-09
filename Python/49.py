def extract_first_element(matrix,index=0):
    result_elements=[]
    for row in matrix:
        if len(row)>index:
            result_elements.append(row[index])
        else:
            result_elements.append(None)
    return result_elements

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(extract_first_element(matrix,1))
    

