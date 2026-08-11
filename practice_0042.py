# Practicing Drill:
animals = ['lion', 'tiger', 'cheetah']

for number, animal in enumerate(animals, start=1):
    number = (f"{number}.")
    print(number, animal)

delete = int(input("Which one to remove? (enter number): "))
animals.pop(delete - 1)

print(animals)

answer = lambda x, y: x * 10
print(answer)