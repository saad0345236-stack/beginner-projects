# Placing an order:
menu = {
    'burger': 4.99,
    'pizza': 8.99,
    'ice cream': 6.99,
    'salad': 3.99,
    'water bottle': 1.49
}

print(menu, "What would you like?")

order = input("Enter a meal: ").lower()

if order in menu:
    print(f"Here's your {order}. That will be {menu[order]}. Have a nice day!")

else:
    print("Enter an item from the menu.")