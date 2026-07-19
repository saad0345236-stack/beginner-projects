# Creating a test:
answer_1 = input("What's the number that's 6, when multiplyed by 2? ")
if answer_1 == "3":
    print(f"That's correct! {answer_1} is the answer.")
else:
    print("Wrong answer. Move onto the next question.")
print("Interesting start now, Enter the correct answer to the question below:")
answer_2 = input("How many planets are in our solar system? ")
if answer_2 == "8":
    print("Correct answer! Now time for the final question.")
else:
    print("Wrong, there's still 1 last question left...")
answer_3 = input("Can you name which year did humans land on the moon? ")
if answer_3 == "1969":
    print("Correct answer! Thanks for playing. Claim your points below!")
else:
    print("Wrong answer, better luck next time. Claim your points below.")
question = input("How many questions did you get right from '0' to '3'? Enter the digit: ")
if question == "0":
    print("Ouch, better luck next time.")
elif question == "1":
    print("Atleast you tried. Thanks for playing.")
elif question == "2":
    print("Good job!")
elif question == "3":
    print("You won the game! Congratulations on your win.")
else:
    print("Sorry, You're only supposed to enter a digit from 0 to 3.")