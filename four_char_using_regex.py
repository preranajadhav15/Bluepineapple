import re

def long_words(text):
    pattern = r'\b\w{4,}\b'
    result=re.findall(pattern, text)
    return result
print(long_words("i am prerana jadhav from pune"))
