# 07 - Exclusive Or
def xor(value1, value2):
    return bool((value1 or value2) and not (value1 and value2))


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
