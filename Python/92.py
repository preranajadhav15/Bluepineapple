def is_undulating(num):
    s=str(num)
    if len(s)<3 or s[0]==s[1]:
        return "not undulating number"
    for i in range (2,len(s)):
        if(s[i]!=s[i % 2]):
            return "not undulating number"
    return "Undulating number"

num=121
print(is_undulating(num))