def binary_to_decimal(binary_num):

    decimal = 0
    power = 0

    binary_str=str(binary_num)
    binary_reversed=reversed(binary_str)

    for i in binary_reversed:
        decimal += int(i) * (2 ** power)
        power += 1

    return decimal
print(binary_to_decimal(1101))
