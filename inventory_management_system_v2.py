# Inventory management system of a store (version 2):
try:
    number = 0
    products = []
    while True:
        menu = input("MAIN MENU: 'add product', 'sell product', 'check products' or 'quit': ").lower()
        if menu == 'add product':
            name = input("Name: ")
            price = input("Price: ")
            number += 1
            entry = f"{number}. {name}: ${price} | "
            print("Current inventory:")
            products.append(entry)
            print(''.join(products))
        elif menu == 'sell product':
            item = int(input("Which item do you want to sell? (base unit number): "))
            to_delete = item - 1
            products.pop(to_delete)
            print(''.join(products))
        elif menu == 'check products':
            print("Here's the inventory:")
            print(''.join(products))
        elif menu == 'quit':
            print("You left the menu.")
            break
        else:
            print("Invalid, you're going to be redirected to the main menu.")
            pass
except ValueError:
    print("Invalid.")