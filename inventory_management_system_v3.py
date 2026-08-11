# Inventory management system of a store (version 3, final version):
try:
    products = []
    while True:
        menu = input("MAIN MENU: 'add product', 'sell product', 'check products' or 'quit': ").lower()
        if menu == 'add product':
            to_add = input("Enter name & price in the format '(Name): $(Price)': ")
            print("Current inventory:")
            products.append(to_add)
            for number, item in enumerate(products, start=1):
                print(number, item)
        elif menu == 'sell product':
            item = int(input("Which item do you want to sell? (base unit number): "))
            to_delete = item - 1
            products.pop(to_delete)
        elif menu == 'check products':
            print("Here's the inventory:")
            print(products)
        elif menu == 'quit':
            print("You left the menu.")
            break
        else:
            print("Invalid, you're going to be redirected to the main menu.")
            pass
except (ValueError, IndexError):
    print("Invalid.")