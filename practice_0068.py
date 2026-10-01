# Practicing Session:
while True:
    n = int(input("Height: "))
    if n > 0:
        break

for i in range(n):
    print('#')

print('?' * 4)

for i in range(3):
    print('#' * 3)

scores = []

for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

avg = sum(scores) / len(scores)
print(f"Average: {avg}")

names = [
    {'name': "kelly", 'number': "1000"},
    {'name': "john", 'number': "1001"}
]

name = input("Enter name: ").lower()

for person in names:
    if person['name'] == name:
        number = person['number']
        print(f"{name}. {number}")
        break
else:
    print("Not found.")