def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact


def binomial_coefficient(a,b):
    result=factorial(a)/(factorial(b)*factorial(a-b))
    return result
print(binomial_coefficient(10,4))
