# Offering a vegan and non–vegan menu:
choice = input("Are you a vegan, yes or no? ")
if choice == "yes":
    print("Here's the vegan options:")
    print("Hummus & pita")
    print("Falafel")
    print("Veggie stir–fry")
    print("Guacamole & chips")
elif choice == "no":
    print("Here's the non–vegan options:")
    print("Burger")
    print("Chicken sandwich")
    print("Omelet")
    print("Steak")
else:
    print("Invalid answer.")
print("Have a nice day.")