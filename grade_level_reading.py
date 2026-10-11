# Grade–Level Reading:
try:
    grade = int(input("Enter a Grade: "))
    
    if grade == 1:
        print("One fish, two fish. Red fish, blue fish.")
    elif grade == 2:
        print("The big dog barked loudly in a park.")
    elif grade == 3 or grade == 4:
        print("We packed lunch and traveled to the sandy beach for a family picnic.")
    elif grade == 5 or grade == 6:
        print("Although the storm brought heavy rain, our sturdy wooden cabin remained safe and warm through the night.")
    elif grade == 7 or grade == 8:
        print("After conducting several scientific experiments, the students concluded that the chemical solution changed colors when heated.")
    elif grade == 9 or grade == 10:
        print("Environmental scientists argue that implementing strict conservation policies is absolutely vital to safeguarding ecosystems from climate damage.")
    else:
        print("Pick a grade from 1 to 10.")

except ValueError:
    print("You can only enter a grade number from 1 to 10.")