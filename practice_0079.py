# Practicing Session:
cities = {
    "China": "Beijing",
    "United States": "Washington D.C.",
    "Japan": "Tokyo"}

print(cities['China'])
print(cities.get('Russia'))
print(cities.keys())
print(cities.values())
print(cities.items())
print(cities.update({"France": "Paris"}))
print(cities.update({"United States": "Seattle"}))
print(cities.pop("Japan"))

for key, value in cities.items():
    print(key, value)

print(cities.clear())

name = "jacob"

if (name[0].islower()):
    print(name.capitalize())