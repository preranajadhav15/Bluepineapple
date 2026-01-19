def newman_convey(n):
    if n==1 or n==2:
        return 1
    else:
         return newman_convey(newman_convey(n-1))+newman_convey(n-newman_convey(n-1))
print(newman_convey(5))
    