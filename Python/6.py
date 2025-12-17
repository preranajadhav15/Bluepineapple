def differ_at_one_bit(num1,num2):
    num=num1^num2
    num3=bin(num)
    count=0
    for i in range(len(num3)):
        if num3[i]=="1":
            count=count+1

    if count==1:
        print("Differ by one bit")
    else:
        print("Not differ by one bit")

differ_at_one_bit(1,2)
