# 11 - Get Middle Character
def center_of(string: str) -> str:
    length = len(string)
    center_index = length // 2
    if length % 2 == 0:
        return string[center_index - 1 : center_index + 1]
    return string[center_index]


print(center_of("I Love Python!!!") == "Py")  # True
print(center_of("Launch School") == " ")  # True
print(center_of("Launchschool") == "hs")  # True
print(center_of("Launch") == "un")  # True
print(center_of("Launch School is #1") == "h")  # True
print(center_of("x") == "x")  # True
