def multiples_number(n, m):
    multiples = []
    for i in range(1, m + 1):
        multiples.append(n * i)
    return multiples
print(multiples_number(2,5))
