def nth_term_geometric_series(a,r,n):
    if n<1:
        return "none"
    else:
        return a*(r**(n-1))
print(nth_term_geometric_series(2,3,4))