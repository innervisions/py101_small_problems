# 10 - What Century is That?
def prefix(century:int) -> str:
    digits = str(century)
    ones = digits[-1]
    tens = digits[-2] if century > 9 else "0"
    
    if tens == "1":
        return "th"
    match ones:
        case "1":
            return "st"
        case "2":
            return "nd"
        case "3":
            return "rd"
    return "th"


def century(year:int) -> str:
    century = year // 100
    if year % 1000 != 0:
        century += 1
    return str(century) + prefix(century)

print(century(2000) == "20th")  # True
print(century(2001) == "21st")  # True
print(century(1965) == "20th")  # True
print(century(256) == "3rd")  # True
print(century(5) == "1st")  # True
print(century(10103) == "102nd")  # True
print(century(1052) == "11th")  # True
print(century(1127) == "12th")  # True
print(century(11201) == "113th")  # True
