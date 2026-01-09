def diff_sum_even_odd(num):
    even_sum=0
    odd_sum=0
    for i in range(1,num+1):
        if i%2==0:
            even_sum+=i
            
        else:
            odd_sum+=i
    return abs(even_sum-odd_sum)
print(diff_sum_even_odd(5))