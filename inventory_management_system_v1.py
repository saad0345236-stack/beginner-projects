# Inventory management system of a store (version 1):
try:
    products = []
    while True:
        menu = input("MAIN MENU: 'add product', 'check products' or 'quit': ").lower()
        if menu == 'add product':
            name = input("Name: ")
            price = input("Price: ")
            products.append(name)
            products.append(': $')
            products.append(price)
            products.append('|')
            print("Current inventory:")
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