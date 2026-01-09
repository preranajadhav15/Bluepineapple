def first_last_char_same(string):
   string1=string.lower()
   if len(string)>0 and string1[0]==string1[-1]:
      return True
   else :
      return False
print(first_last_char_same("Area"))
