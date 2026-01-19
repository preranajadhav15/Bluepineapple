def max_product_from_tuple(lst):
    return max([i*j for (i,j) in lst], default=None)
lst=[(1,2),(3,2),(4,5),(6,4)]
print(max_product_from_tuple(lst))