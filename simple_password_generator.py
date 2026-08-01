# Creating a letter and digit password generator
import random
import string

count = 0
password_list = []
while count < 4:
    letter = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    password_list.append(letter)
    password_list.append(digit)
    count += 1
print(''.join(password_list))