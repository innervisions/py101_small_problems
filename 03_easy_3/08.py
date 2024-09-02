# 8 - Grade Book
def get_grade(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"

print(get_grade(95, 90, 93) == "A")  # True
print(get_grade(50, 50, 95) == "D")  # True
