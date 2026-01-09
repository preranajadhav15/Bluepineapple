def max_difference(lists):
    return max(map(lambda x: abs(x[0]-x[1]),lists)) 
lists=[[2,1],[10,2],[3,4]]
print(max_difference(lists))
