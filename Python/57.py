def largest_number_formed(digits):
    result=''
    digits.sort()
    
    for i in digits:
        result+=str(i)
    return result[::-1]

print(largest_number_formed([1,4,3,7]))