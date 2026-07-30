# Rock, paper, scissors game:
import random

picks = ('rock', 'paper', 'scissor')
emojis = { 'rock': '🪨', 'paper': '📄', 'scissor': '✂️'}

while True:
    try:
        comp_pick = random.choice(picks)
        user_pick = input("Rock, paper, scissor? ").lower()
        if user_pick not in picks:
            print("Invalid choice!")
            continue

        print(f"You chose {emojis[user_pick]}")
        print(f"I chose {emojis[comp_pick]}")
        
        if user_pick == comp_pick:
            print("TIE!")
        elif (
            (user_pick == 'rock' and comp_pick == 'scissor') or
            (user_pick == 'paper' and comp_pick == 'rock') or
            (user_pick == 'scissor' and comp_pick == 'paper')):
                print("YOU WON!")
        else:
            print("YOU LOST!")
        again = input("New game? (yes/no): ").lower()
        if again == 'no':
            print("Thanks for playing!")
            break
    
    except KeyError:
        print("Try again.")