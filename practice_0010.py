# Making a number guessing game with Planets:
answer = 5
guess_count = 0
guess_limit = 3
print("Let's play a guessing game. You get 3 guesses to guess a single digit number.")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == answer:
        print("You win!")
        break
    else:
        print("wrong...")
else:
    print("You failed.")