def is_number_diff_of_squares(num):
    for i in range(1,int(num**0.5)+2):
        for j in range(i):
            if i*i - j*j==num:
                return "Yes number can be represent as difference of squares of two number"
    return "Cannot represent."
print(is_number_diff_of_squares(40))
print(is_number_diff_of_squares(34))
