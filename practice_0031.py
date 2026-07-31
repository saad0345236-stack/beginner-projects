# Modularizing the Rock, paper, scissors game:
import random

emojis = { 'rock': '🪨', 'paper': '📄', 'scissor': '✂️' }
picks = tuple(emojis.keys())

def get_user_pick():
    while True:
        user_pick = input("Rock, paper, scissor? ").lower()
        if user_pick in picks:
            return user_pick
        else:
            print("Invalid answer!")

def choices(user_pick, comp_pick):
    print(f"You chose {emojis[user_pick]}")
    print(f"I chose {emojis[comp_pick]}")

def winner(user_pick, comp_pick):
    if user_pick == comp_pick:
        print("TIE!")
    elif (
        (user_pick == 'rock' and comp_pick == 'scissor') or
        (user_pick == 'paper' and comp_pick == 'rock') or
        (user_pick == 'scissor' and comp_pick == 'paper')):
        print("YOU WON!")
    else:
        print("YOU LOST!")
        
def game():
    while True:
        
        comp_pick = random.choice(picks)
        
        user_pick = get_user_pick()
        
        choices(user_pick, comp_pick)
        
        winner(user_pick, comp_pick)
        
        again = input("New game? (yes/no): ").lower()
        if again == 'no':
            print("Thanks for playing!")
            break
        
game()