# 12 - Negative
# def negative(number):
#     if number > 0:
#         return -number
#     return number
def negative(number):
    return -abs(number)

print(negative(5) == -5)  # True
print(negative(-3) == -3)  # True
print(negative(0) == 0)  # True
