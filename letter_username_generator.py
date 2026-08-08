# Username generator with letters:
import random
import string

length = int(input("How long should the username be? (use int): "))
limit = 0
name = []

while limit < length:
    username = random.choice(string.ascii_letters)
    name.append(username)
    limit += 1
print(f"{''.join(name)} is your username.")