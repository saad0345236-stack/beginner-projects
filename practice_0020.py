# Practicing 'exceptions':
try:
    age = int(input('Age: '))
    savings = 1000000
    division = savings / age
    print(f"Age is {age} and savings are {savings}.")
    name = input("Enter name:")
    print(f"Your name is {name}.")
    number = int(input("Enter number: "))
    dividing = 2 / number
    print(dividing)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("The input cannot be 0.")