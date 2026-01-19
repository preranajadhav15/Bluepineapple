def eulerian_number(n,m):
    if m>=n or n==0:
        return 0
    if m==0:
        return 1
    return (n-m)*eulerian_number(n-1,m-1)+(m+1)*(eulerian_number(n-1,m))

print(eulerian_number(3,1))