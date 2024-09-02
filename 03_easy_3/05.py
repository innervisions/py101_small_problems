# 5 - Right Triangles
def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')


triangle(5)
print("\n")
triangle(9)
print("\n")
triangle(12)
print("\n")
triangle(50)
