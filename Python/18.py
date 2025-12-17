def remove_chars(str1, str2):
    result = ""
    for char in str1:
        if char not in str2:
            result += char
    return result
str1 = "prerana"
str2 = "jadhav"
print(remove_chars(str1, str2))
