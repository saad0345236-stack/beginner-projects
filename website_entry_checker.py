# Checking if user is eligible to enter a website:
def enter_website(age, answer):
    if age >= 13:
        print("Age is valid.")

        if answer == 'y':
            print("You've agreed to our policies.")
            print("You can enter the website.")
        
        else:
            print("You haven't agreed to our policies.")
            print("You can't enter the website.")
    
    else:
        print("Age is invalid.")
        print("You can't enter the website.")

age = int(input("Enter age: "))
answer = input("Do you agree to our privacy policies? (y/n): ").lower()

enter_website(age, answer)