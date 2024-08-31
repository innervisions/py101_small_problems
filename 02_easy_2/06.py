# 05 - The End Is Near But Not Here
def penultimate(text:str) -> str:
    return text.split()[-2]

def middle_word(text:str):
    words = text.split()
    if not words:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        mid = len(words) // 2

        if len(words) % 2 == 0:
            return [words[mid - 1], words[mid]]
        else:
            return words[mid]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
print(middle_word("") == "")
print(middle_word("hello") == "hello")
print(middle_word("hello world") == ["hello", "world"])
print(middle_word("all cows eat grass") == ["cows", "eat"])
print(middle_word("every good boy does fine") == "boy")
