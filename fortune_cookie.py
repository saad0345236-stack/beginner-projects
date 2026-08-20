# Fortune Cookie:
import random

fortunes = ['A small opportunity can be something bigger', 'A little bit of patience might lead you to something big', 'Your laziness might actually be a symptom of exhaustion not avoidance', 'Action leads to motivation, not the other way around']

question = input("Do you want to see your fortune? (y/n): ").lower()

if question == 'y':
    print(f'Your fortune is "{random.choice(fortunes)}".')

elif question == 'n':
    print("Okay, have a nice day!")

else:
    print("Enter 'y' or 'n'.")