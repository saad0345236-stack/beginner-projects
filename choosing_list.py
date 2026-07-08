# Providing user a choice between 2 lists:
asking = input("Would you like a list of planets or continents? ")
if asking.upper() == "PLANETS":
    print("1. Mercury")
    print("2. Venus")
    print("3. Earth")
    print("4. Mars")
    print("5. Jupiter")
    print("6. Saturn")
    print("7. Uranus")
    print("8. Neptune")
elif asking.upper() == "CONTINENTS":
    print("1. North America")
    print("2. South America")
    print("3. Europe")
    print("4. Africa")
    print("5. Asia")
    print("6. Australia")
    print("7. Antarctica")
else:
    print("Invalid answer.")