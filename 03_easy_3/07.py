# 7 - Double Double
def is_double(number):
    digits = str(number)
    middle = len(digits) // 2
    return digits[0:middle] == digits[middle:]

def twice(number):
    return number if is_double(number) else number * 2

print(twice(37) == 74)  # True
print(twice(44) == 44)  # True
print(twice(334433) == 668866)  # True
print(twice(444) == 888)  # True
print(twice(107) == 214)  # True
print(twice(103103) == 103103)  # True
print(twice(3333) == 3333)  # True
print(twice(7676) == 7676)  # True
