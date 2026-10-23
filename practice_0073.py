# Practicing Drill:
import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi), math.ceil(pi), math.floor(pi), abs(pi), pow(pi, 2), math.sqrt(pi), max(x, y, z), min(x, y, z))

name = 'Christopher Columbus'

first_name = name[:11]
last_name = name[12:]

print(first_name, last_name)

country = input("Enter country: ")
country_age = int(input("How old is said country?: "))
height = float(input("How tall are you? (cm): "))

print("You picked the country", country)
print("Your country is " + str(country_age) + " years old")
print(f"You're {height}cm tall")