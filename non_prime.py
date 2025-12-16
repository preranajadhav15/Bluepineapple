def non_prime(start,end):
    nonprime=[]
    for num in range(start,end+1):
        for i in range(2,num):
            if num%i==0:
                nonprime.append(num)
                break
    return nonprime
print(non_prime(1,10))
