def largest_prime_factor(num):
    largest_factor=0
    i=2
    while i*i<=num:
        if num%i==0:
            largest_factor=i
            num//=i
        else:
            i+=1
    if num>1:
        largest_factor=num
    return largest_factor

print(largest_prime_factor(57))