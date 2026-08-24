# Practicing Drill:
import random

def coin_toss():
    outcomes = "HEADS", "TAILS"
    result = random.choice(outcomes)

    return f"'{result}' is the result of the coin toss!"

choice = input("Do you want to flip a coin? (y/n): ").lower()

if choice == 'y':
    print(coin_toss())

elif choice == 'n':
    print("Okay, have a good day.")

else:
    print("Enter either 'y' or 'n'.")