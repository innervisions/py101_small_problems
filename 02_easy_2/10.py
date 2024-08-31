# 10 - When Will I Retire?
import datetime

current_age = int(input("What is your age?: "))
retirement_age = int(input("At what age would you like to retire?: "))
current_year = datetime.date.today().year
years_to_retirement = retirement_age - current_age

print(
    f"\nIt's {current_year}. "
    f"You will retire in {current_year + years_to_retirement}.\n"
    f"You only have {years_to_retirement} years of work to go!"
)
