# Receipt splitter:
def split(total, tip, people):
    total_amount = total + tip

    try:
        per_person = total_amount / people

        return print(f"Original Bill: ${total}. Tip: ${tip}. Total with tip: ${total_amount}. Each person gives: ${per_person}.")

    except ZeroDivisionError:
        print("Enter a positive number higher than 0.")

try:
    total = int(input("Enter total: "))

    tip = int(input("Enter tip (if there's no tip enter 0): "))

    people = int(input("Enter the # of people: "))

    if total <= 0 or tip < 0 or people <= 0:
        print("Enter a positive number higher than 0.")
    
    else:
        split(total, tip, people)

except ValueError:
    print("Please enter positive integers.")