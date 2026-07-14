# Practicing nested loops:
for a in range(3):
    for b in range(2):
        print(f"({a}), ({b})")
# Practicing Lists:
names = ['Henry', 'Sara', 'Tom']
names[1] = 'Sarah'
print(names)
print(names[1:3])
print(names[:])
print(names[1:2])
# Printing coordinates:
for x in range(4):
    for y in range(3):
        for z in range(2):
            print(f"({x}), ({y}), ({z})")