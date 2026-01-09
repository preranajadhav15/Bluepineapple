import re
def split_with_multiple_delimiters(string,delimiters):
    result=re.split(f"[{re.escape(delimiters)}]+",string)
    return result
string="hi prerana! how are you doing? well and good" 
delimiters='!,?'
print(split_with_multiple_delimiters(string,delimiters))