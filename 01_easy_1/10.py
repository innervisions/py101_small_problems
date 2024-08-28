# 10 - Multiples of 3 and 5

def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(number):
    sum = 0
    for index in range(1, number + 1):
        if is_multiple(index, 3) or is_multiple(index, 5):
            sum += index
    return sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
