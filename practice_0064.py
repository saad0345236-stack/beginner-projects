# Practicing Drill:
digits = []

while True:
    question = input("Do you want to add a number to the list? (y/n): ").lower()

    if question == 'y':
        try:
            digit = int(input("Enter digit: "))

            digits.append(digit)

            digits.sort()
            print(digits)
        
        except ValueError:
            print("You can only enter integers.")
    
    elif question == 'n':
        print("Okay.")
        break
    
    else:
        print("Sorry, you can only reply with 'y' or 'n'.")