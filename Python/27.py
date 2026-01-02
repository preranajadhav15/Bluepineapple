def remove_num(string):
    string_without_number=""
    for i in string:
        if not i.isdigit():
            string_without_number+=i
    return string_without_number

print(remove_num("prerana15"))
