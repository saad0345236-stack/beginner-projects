# Practicing Drill:
try:
    def give_sum(numbers):
        return print(sum(numbers))

    numbers = int(input("Enter numbers: "))
    
    give_sum(numbers)

except ValueError:
    print("Please enter positive numbers.")

except TypeError:
    print("Enter 2 elements.")

try:
    def double(number):
        return print(2 * number)
        
    number = int(input("Enter a number: "))
    
    double(number)
    
except ValueError:
    print("Enter an integer.")