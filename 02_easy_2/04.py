# 04 - Squaring an Argument
def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def power(base, exponent):
    result = 1
    for index in range(exponent):
        result = multiply(result, base)
    return result

print(square(5) == 25)  # True
print(square(-8) == 64)  # True
print(power(2, 0) == 1)
print(power(2, 1) == 2)
print(power(2, 2) == 4)
print(power(2, 3) == 8)
print(power(2, 4) == 16)
