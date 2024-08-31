# 08 - Odd Lists
# def oddities(lst:list):
#     new_list = []
#     index = 0
#     while index < len(lst):
#         new_list.append(lst[index])
#         index += 2
#     return new_list

def oddities(lst:list):
    return lst[::2]

def evenities(lst:list):
    return lst[1::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])  # True
print(oddities(["abc", "def"]) == ["abc"])  # True
print(oddities([123]) == [123])  # True
print(oddities([]) == [])  # True

print()

print(evenities([2, 3, 4, 5, 6]) == [3, 5])  # True
print(evenities([1, 2, 3, 4]) == [2, 4])  # True
print(evenities(["abc", "def"]) == ["def"])  # True
print(evenities([123]) == [])  # True
print(evenities([]) == [])  # True
