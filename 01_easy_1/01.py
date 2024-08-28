## 01 - Isn't it Odd?
def is_odd(number: int) -> bool:
    return abs(number) % 2 == 1

print(is_odd(4))
print(is_odd(0))
print(is_odd(1))
print(is_odd(-2))
