def binary_to_decimal(binaryStr):
    decimal = 0
    for i in range(0, len(binaryStr)):
        decimal += int(binaryStr[len(binaryStr) - i - 1]) * (2 ** i)
    return decimal

print binary_to_decimal('10101')