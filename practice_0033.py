# Making a password generator for practice:
import random
import string

print("Hello! This is a password generator.")
try:
    limit = int(input("How many characters should the password to be? "))
    characters = 0
    password_list = []
    while characters < limit:
        letters1 = random.choice(string.ascii_lowercase)
        letters2 = random.choice(string.ascii_uppercase)
        digits = random.choice(string.digits)
        punctuation = random.choice(string.punctuation)
        password_list.append(letters1)
        password_list.append(letters2)
        password_list.append(digits)
        password_list.append(punctuation)
        characters += 1
    
    password = "".join(password_list)
    
    print(password[:limit])
    print("This is your password. Keep it secure!")

except ValueError:
    print("The answer must be an integer.")