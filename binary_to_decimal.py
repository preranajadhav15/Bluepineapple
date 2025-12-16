def binary_to_decimal(binary_str):
    decimal = 0
    power = 0

    for digit in reversed(binary_str):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal
print(binary_to_decimal("1101"))
