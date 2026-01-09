import re
def lowercase_with_underscore(text):
    pattern=r"\b[a-z]+(?:_[a-z]+)+\b"
    sequence=re.findall(pattern,text)
    return sequence
print(lowercase_with_underscore("Prerana_15 f_f  user_ame"))

