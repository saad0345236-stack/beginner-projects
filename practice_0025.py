# Generating random values:
import random
for item in range(5):
    print(random.random())
for item in range(3):
    print(random.randint(0, 100))
people = ['Jake', 'Mike', 'Chloe', 'Joe', 'Amy']
team_leader = random.choice(people)
print(team_leader)
# Rolling a dice:
class Dice:
    def roll(self):
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)
        return n1, n2
dice = Dice()
print(dice.roll())