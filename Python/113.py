def is_integer_string(string):
    if string.startswith(('+','-')):
        string=string[1:]
    return string.isdigit()
print(is_integer_string('-123'))
print(is_integer_string('123'))
print(is_integer_string('abc'))
