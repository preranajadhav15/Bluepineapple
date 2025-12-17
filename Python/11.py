def remove_first_last(string,ch):
    result=""
    count=0

    for i in string:
        if i==ch:
            count+=1

            if count==1 or count==string.count(ch):
                continue

        result+=i
    return result
print(remove_first_last("banana","a"))
