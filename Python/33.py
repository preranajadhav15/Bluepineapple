def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary = ""
    while decimal_number > 0:
        remainder = decimal_number % 2        
        binary = str(remainder) + binary      
        decimal_number = decimal_number // 2  
    return binary
print(decimal_to_binary(13))
