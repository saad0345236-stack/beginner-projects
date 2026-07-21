# Guessing game:
print("Guess a number from 0 to 10. You only get 2 guesses, but you can also earn an additional guess, if you fail.")
import random
answer = random.randint(0, 10)
guesses = 2
guess_1 = int(input("> "))
while guesses > 0:
    if guess_1 == answer:
        print("You win!")
        break
    else:
        new_guess = guesses - 1
        guess_2 = int(input(f"Ouch, you now have {new_guess} guess left. Next guess? "))
        if guess_2 == answer:
            print("You won!")
            break
        else:
            final_guess = new_guess - 1
            print("You lost!")
            ask = input("Do you want a last chance? Type either 'yes' or 'no': ").lower()
            if ask == "yes":
                print("Okay. Enter your final guess!")
                last_try = int(input("> "))
                if last_try == answer:
                    print("You did it! You win!")
                    break
                else:
                    print("GAME OVER!")
                    break
            else:
                print("You still made a good effort!")
                break