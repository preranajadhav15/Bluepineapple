def twice_reverse(num):
    original=num
    reverse=0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num//=10
    result=(2*reverse)-1
    if original==result:
        return True
    return False
print(twice_reverse(45))