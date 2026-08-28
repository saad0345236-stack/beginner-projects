# Practicing Drill:
def double_evens(number):
    if number % 2 == 0:
        return f"{number * 2} is double of {number}."
    
    else:
        return f"{number} is unchanged."

try:
    number = int(input("Enter number: "))
    
    print(double_evens(number))

except ValueError:
    print("You can only enter integers.")