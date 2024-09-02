# 04 - String Strings
def stringy(length):
    result = ""
    bit = 1
    for _ in range(length):
        result += str(bit)
        bit = abs(bit - 1)
    return result


print(stringy(6) == "101010")  # True
print(stringy(9) == "101010101")  # True
print(stringy(4) == "1010")  # True
print(stringy(7) == "1010101")  # True
