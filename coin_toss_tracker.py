# Coin toss tracker:
import random

def coin_toss(times):
    outcomes = ["HEADS", "TAILS"]

    limit = 0
    results = []

    while limit < times:
        result = random.choice(outcomes)
        results.append(result)
        limit += 1
    
    heads = 0
    tails = 0

    for output in results:
        if output == 'HEADS':
            heads += 1
        else:
            tails += 1
    
    answer = f"No. of tosses: {times}."
    tosses = f"HEADS: {heads} & TAILS: {tails}"

    return f"{answer} | {tosses}"

choice = input("Do you want to flip a coin? (y/n): ").lower()

if choice == 'y':
    times = int(input("How many? "))
    print(coin_toss(times))

elif choice == 'n':
    print("Okay, have a good day.")

else:
    print("Enter either 'y' or 'n'.")