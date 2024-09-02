# 9 - Clean Up the Words
def clean_up(string:str):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
        elif not result.endswith(" "):
            result += " "
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True
