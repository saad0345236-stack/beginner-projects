# Practicing Drill:
def check_password(password):

    question = input("What is the password? ")

    if question == password:
        return f"{question} is the correct password."
    
    else:
        return f"That is the incorrect password."

passcode = input("Enter password: ")

print(check_password(passcode))