# Practicing Drill:
def valid_password(passcode):
    characters = passcode
    count = 0

    for character in characters:
        count += 1
        pass

    if count >= 8:
        print("Password is atleast 8 characters✓")
    else:
        print("Passcode needs atleast 8 characters.")

    has_digit = False
    for character in passcode:
        if character.isdigit():
            has_digit = True
            break

    if has_digit:
        print("Passcode has atleast one digit✓")

    else:
        print("Passcode needs atleast one digit.")
    
    if count >= 8 and has_digit:
        print(f"{passcode} is valid!")
    else:
        print(f"{passcode} isn't valid.")

entry = input("Enter password: ")

valid_password(entry)