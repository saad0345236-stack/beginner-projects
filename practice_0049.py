# Practicing Drill:
name = input("Username: ").lower()

name_list = [name]

username = name.replace(' ', '_')

if len(username) >= 5 and len(username) <= 15:
    print(f"{username} is a valid username.")
    choice = input("Would like to reverse this username backwards? (y/n): ").lower()

    if choice == 'y':
        print(f"{username[::-1]} is the new username.")

    elif choice == 'n':
        print("Understood.")
    
    else:
        print("Invalid answer.")

else:
    print(f"{username} is an invalid username.")