def sort_matrix(matrix):
    rows = len(matrix)

    for i in range(rows):
        for j in range(i + 1, rows):
            if sum(matrix[i]) > sum(matrix[j]):
                matrix[i], matrix[j] = matrix[j], matrix[i]

    return matrix


matrix=[[1,6,3],[1,3,2],[2,-3,1]]
print(sort_matrix(matrix))
