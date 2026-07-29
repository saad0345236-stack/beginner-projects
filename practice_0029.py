# Dice rolling game:
import random

while True:
    choice = input("Roll the dice? (yes/no): ").lower()
    if choice == 'yes':
        print(f"({random.randint(1,6)}, {random.randint(1, 6)})")
    elif choice == 'no':
        print("Thanks for playing")
        break
    else:
        print("Invalid answer.")
# Number guessing game:
answer = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess a number from 1 to 100: "))
        if guess > answer:
            print("Too high!")
        elif guess < answer:
            print("Too low!")
        elif guess == answer:
            print("You won!")
            break
        else:
            print("Invalid answer.")
    except ValueError:
        print("Invalid answer.")