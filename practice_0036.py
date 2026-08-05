# Practicing drill:
countries = []
countries.append('United Kingdom')
countries.append('France')
countries.append('Germany')
print(countries)
countries.pop(2)
print(countries)
try:
    entry = input()
    answer = 2 * int(entry)
    print(answer)
except ValueError:
    print("Invalid value.")