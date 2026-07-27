# Calculating user's age in the upcoming years:
from datetime import date
current_year = date.today().year
print("Enter a year and we'll calculate how old you'll be in that future year.")
try:
    age = int(input("Enter age: "))
    year = int(input("Enter year: "))
    calc = age + (year - current_year)
    print(f"You'll be {calc} years old in {year}.")
except ValueError:
    print("Invalid answer.")