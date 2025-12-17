def dominoes(num):
    
    if num%2!=0:
        print("This code is run for only even number of n")
        return 0

    if num==0:
        return 1

    if num==2:
        return 3

    num2=1
    num1=3

    for i in range(4,num+1,2):
        ways=4*num1-num2
        num2=num1
        num1=ways
    return num1

num=int(input("Enter the value of n:"))
print("number of wyas of fill dominoe:",dominoes(num))

    
