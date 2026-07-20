# Creating a simple calculator:
print("You can enter any 2 values to perform 1 of 4 different arithmetic operations.")
try:
    value_1 = int(input("1st value? "))
    value_2 = int(input("2nd value? "))
    choice = input("Type one of the following '+', '-', '*' & '/': ")
    if choice == "+":
        add = value_1 + value_2
        print(f"Answer is {add}.")
    elif choice == "-":
        minus = value_1 - value_2
        print(f"Answer is {minus}.")
    elif choice == "*":
        multiply = value_1 * value_2
        print(f"Answer is {multiply}.")
    elif choice == "/":
        divide = value_1 / value_2
        print(f"Answer is {divide}.")
    else:
        print("Invalid operator.")
except ZeroDivisionError:
    print("You can't divide with 0.")
except ValueError:
    print("Invalid input.")