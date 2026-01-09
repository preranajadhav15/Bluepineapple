def count_substring_equal_sum(string):
    count=0
    n=len(string)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=int(string[j])
            length=j-i+1
            if sum==length:
                count+=1
    return count

string='123123'
print(count_substring_equal_sum(string))