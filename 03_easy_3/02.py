# 2 - ddaaiillyy ddoouubbllee
def crunch(string):
    result = ""
    previous_char = None
    for char in string:
        if char != previous_char:
            result += char
        previous_char = char
    return result

# These examples should all print True
print(crunch("ddaaiillyy ddoouubbllee") == "daily double")
print(crunch("4444abcabccba") == "4abcabcba")
print(crunch("ggggggggggggggg") == "g")
print(crunch("abc") == "abc")
print(crunch("a") == "a")
print(crunch("") == "")
