# Practicing "inheritance":
class Evolution:
    def swim(self):
        print("Swim")
class Shark(Evolution):
    pass
class Whale(Evolution):
    pass
shark1 = Shark()
shark1.swim()
whale1 = Whale()
whale1.swim()
# Practicing functions:
def lbs_to_kg(weight):
    return weight * 0.45
def kg_to_lbs(weight):
    return weight / 0.45
print(kg_to_lbs(65))
print(lbs_to_kg(150))