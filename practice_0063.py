# Practicing Drill:
numbering = 0
numbers = [1, 2, 3]

numbers.append(4)
numbers.append('Jake')
numbers.append(True)

for item in numbers:
    numbering += 1
    print(f"{numbering}. {item}")