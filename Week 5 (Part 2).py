def decimal_to_binary(n:int):
    if n == 0:
        return ''
    q, r = divmod(n, 2)
    return decimal_to_binary(q) + str(r)

def binary_to_decimal(b:str):
    if b == '':
        return 0
    n = len(b) - 1
    pv = 2 ** n
    d = int(b[0])
    v = pv * d
    return v + binary_to_decimal(b.removeprefix(b[0]))

print(binary_to_decimal('1010'))
print(binary_to_decimal("11111111"))
print(binary_to_decimal("1"))
# print(decimal_to_binary(4))
# print(decimal_to_binary(10))   # "1010"
# print(decimal_to_binary(255))  # "11111111"
# print(decimal_to_binary(1))    # "1"