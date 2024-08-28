# 07 - Short Long Short
# def short_long_short(string_1, string_2):
#     if len(string_1) < len(string_2):
#         short_string = string_1
#         long_string = string_2
#     else:
#         short_string = string_2
#         long_string = string_1

#     return short_string + long_string + short_string


def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1


# These examples should all print True
print(short_long_short("abc", "defgh") == "abcdefghabc")
print(short_long_short("abcde", "fgh") == "fghabcdefgh")
print(short_long_short("", "xyz") == "xyz")
