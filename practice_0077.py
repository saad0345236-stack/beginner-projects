# Practicing Session:
countries = ['Canada', 'Brazil', 'Spain', 'Italy', 'Australia']

countries[2] = 'Poland'

print(countries[2])

countries.append('Croatia')
countries.remove('Poland')
countries.pop()
countries.insert(3, 'Greece')
countries.sort()

for country in countries:
    print(country)

countries.clear()
print(countries)

cities = ['Paris', 'London', 'Rome']
continents = ['Africa', 'Antarctica', 'Asia']

places = [cities, continents]
print(places[1][2])