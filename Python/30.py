def count_start_end(string):
    count=0
    for i in range(len(string)):
       for j in range(i+1,len(string)):
           if string[i]==string[j]:
               count+=1
    return count
print(count_start_end("abcabc"))
