import math

def check_woodall(num):
    for n in range (1, int(math.sqrt(num))+1):
        woodall=(n*(2**n))-1
        if woodall==num:
            print("number is woodall")
        if woodall>num & woodall<num:
            print("Not woodall number")
    return 0

print(check_woodall(1))
