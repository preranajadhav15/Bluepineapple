def min_rotations_to_same_string(string):
    rotated = string
    count = 0

    while True:
        rotated = rotated[1:] + rotated[0]   
        count += 1

        if rotated == string:
            return count
print(min_rotations_to_same_string("abcd"))
