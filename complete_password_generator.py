# Making a complete password generator:
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters)
    for character in range(length))

print("Hello! This is a password generator.")

try:
    limit = int(input("How many characters should the password to be? "))
    password = generate_password(limit)
    print(password)
    print("This is your password. Keep it secure!")

except ValueError:
    print("The answer must be an integer.")