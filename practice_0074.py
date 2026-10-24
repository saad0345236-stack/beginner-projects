# Practicing Drill:
city = "London"
new_city_name = city[::2]
reversed_name = city[::-1]

print(new_city_name, reversed_name)

website_1 = "https//google.com"
website_2 = "https//wikipedia.com"

sliced = slice(7, -4)

print(website_1[sliced], website_2[sliced])

age = int(input("How old are you? "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult.")
elif age <= 0:
    print("You haven't been born yet!")
else:
    print("You are not an adult.")