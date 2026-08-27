# Expense Tracker:
expense = []

def manage_expenses():
    try:
        choice = input("Do you want to add expense, view expenses or see total? (add/view/total): ").lower()
        
        if choice == 'add':
            new_expense = int(input("Enter expense: "))
            expense.append(new_expense)
            
        elif choice == 'view':
            print(expense)
            
        elif choice == 'total':
            print(f"${sum(expense)}")
            
        else:
            print("Sorry, I don't understand that.")
    
    except ValueError:
        print("Enter an integer.")

while True:
    decision = input("Do you want to use 'expense' function? (y/n): ").lower()

    if decision == 'y':
        manage_expenses()
    
    elif decision == 'n':
        break
    
    else:
        print("You can only enter 'y' or 'n'.")