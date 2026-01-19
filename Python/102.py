def snake_to_camel(string):
    camel=''
    upper=False
    for i in string:
        if i=='_':
            upper=True
        else:
            camel+=i.upper() if upper else i
            upper=False
    return camel
print(snake_to_camel("snake_to_camel"))