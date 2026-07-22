# Letting user create a fictional creature:
class Creature:
    def __init__(self, name):
        self.name = name
    def attack(self):
        print("It attacks and successfully captures its prey!")
    def take_damage(self):
        print(f"{self.name} gets injured!")
name = input("Name? ")
print(f"It's name is {name}.")
creature1 = Creature(name)
print("Let's see how it attacks and takes damage.")
ask_1 = input("Do you want to see it attack? type 'yes' or 'no': ").lower()
if ask_1 == "yes":
    creature1.attack()
    print(f"{name} lives to fight another day.")
    print("GAME FINISHED")
elif ask_1 == "no":
    creature1.take_damage()
    print (f"It succumbs to its injuries.")
    print("GAME OVER")
else:
    print("The attack will not be displayed.")