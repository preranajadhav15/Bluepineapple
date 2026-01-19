def shortlist_words(lst: str,length: int) -> int:
    result=[]
    for i in lst:
        if len(i)>length:
            result.append(i)
    return result

if __name__ == "__main__":
    lst=['prerana','maths','python','programming']
    length=5
    print(shortlist_words(lst,length))