def longest_word(lst):
    max_len=0
    word=""
    for i in lst:
        if len(i)>max_len:
            max_len=len(i)
            word=i
    return word
l=["prerana","sakshi","vaishnavi","anushka"]
print(longest_word(l))