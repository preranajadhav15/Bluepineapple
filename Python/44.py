def match_at_beginning(word,string):
    result=string.startswith(word)
    return result
print(match_at_beginning('beg','beginning'))