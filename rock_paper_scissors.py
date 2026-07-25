# Playing rock, paper, scissors with the user:
print("Let's play a game of rock, paper and scissor. Type your pick below:")
import random
class Game:
    def hand(self):
        option = ['rock', 'paper', 'scissors']
        pick = random.choice(option)
        return pick
game = Game()
user_choice = input('>').lower()
comp_choice = game.hand()
print(f"I picked {comp_choice}!")
if user_choice == comp_choice:
    print("IT'S A TIE!")
elif user_choice == 'paper':
    if comp_choice == 'scissors':
        print("I win!")
    else:
        print("You won...")
elif user_choice == 'scissors':
    if comp_choice == 'rock':
        print("I won!")
    else:
        print("fine! you won.")
elif user_choice == 'rock':
    if comp_choice == 'paper':
        print("I win. Better luck next time.")
    else:
        print("Okay, sure. you won.")
else:
    print("But your answer breaks the rules of the game.")