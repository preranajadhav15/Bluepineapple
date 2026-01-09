def adjacent_not_same(string):
    count={}
    for i in string:
        count[i]=count.get(i,0)+1
    for j in count.values():
         if j>((len(string)+1)//2):
              return "Not rearrangable"
    return "Rearrangable"

        
print(adjacent_not_same("Preranaaaaaaa"))