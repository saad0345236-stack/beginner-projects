# Allowing a user to create a list of items and charging the user:
item_list = []
print("This is a shop. Please enter any 3 items of your choice below:")
item_list.append(input('> ').capitalize())
item_list.append(input('> ').capitalize())
item_list.append(input('> ').capitalize())
print("These are all your items:")
print(item_list)
print("Enter the individual costs for all 3 items below:")
cost_1 = int(input("1st item: "))
cost_2 = int(input("2nd item: "))
cost_3 = int(input("3rd item: "))
total = cost_1 + cost_2 + cost_3
print(f"Your total is ${total}. Have a nice day!")