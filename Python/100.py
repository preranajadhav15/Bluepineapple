def next_smallest_palindrome(num):
    num+=1
    while str(num)!=str(num)[::-1]:
        num+=1
    return num
print(next_smallest_palindrome(24))
print(next_smallest_palindrome(102))