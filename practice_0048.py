# Practicing Drill:
def divide(digit_1, digit_2):
    division = float(digit_1) / float(digit_2)

    return f"{division} is the answer."

try:
    value_1 = int(input("Enter 1st value: "))
    value_2 = int(input("Enter 2nd value: "))

    print(divide(value_1, value_2))

except ValueError:
    print("You can only enter integers.")

except ZeroDivisionError:
    print("You can't divide by 0.")

def calculate_area(length, width):
    if length and width > 0:
        return f"{length * width} is the area."
    else:
        print("Both values have to be positive. Unless the output will be:")

try:
    length = int(input("Length: "))
    width = int(input("Width: "))
    
    print(calculate_area(length, width))

except ValueError:
    print("Enter an integer.")