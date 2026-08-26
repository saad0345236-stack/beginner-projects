# Adventure Game:
points = 0
target = 2

print("Your player wakes up in a forest...")

choice_1 = input("Do you want to go left or right? (l/r): ").lower()

if choice_1 == 'r':
    print("You find a coin. You collect it. You now have 1 point...")
    points += 1

    choice_2 = input("You hear some rustling in the bushes. Are you going to investigate? (y/n): ").lower()

    if choice_2 == 'y':
        print("There is rustling in the bushes. You look around yourself and A WOLF ATTACKS YOU!")
    elif choice_2 == 'n':
        print("You find another coin. You now have 2 points...")
        points += 1
    else:
        print("There is rustling in the bushes. You look around yourself and A WOLF ATTACKS YOU!")

elif choice_1 == 'l':
    print("You go left and find a river flowing. It is dead silent...")

    choice_2 = input("You hear some rustling in the bushes. Are you going to investigate? (y/n): ").lower()

    if choice_2 == 'y':
        print("There is rustling in the bushes. You look around yourself and A WOLF ATTACKS YOU!")
    elif choice_2 == 'n':
        print("You ignore it and find a coin.")
        points += 1
    else:
        print("There is rustling in the bushes. You look around yourself and A WOLF ATTACKS YOU!")

else:
    print("There is rustling in the bushes. You look around yourself and A WOLF ATTACKS YOU!")

print("You start to feel dizzy and eventually faint...")

print("Game is over. Let's see if you collected enough coins.")

if points == target:
    print("YOU WON! YOU COLLECTED ENOUGH COINS!")
else:
    print("You lost. You didn't meet the target...")