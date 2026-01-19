def is_substring_present(lst,substring):
    for i in lst:
        if substring in i:
            return True
    return False
l=['prerana','programming','python']
substring='gram'
print(is_substring_present(l,substring))