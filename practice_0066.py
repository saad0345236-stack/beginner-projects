# Practicing Drill:
print("Hello!")

name = input("Enter name: ")
print(f"Hello, {name}!")

def size():
    return len(name)


def unload():
    return True

print(size(), unload())
print("Hello", end='\n')

x = int(input("X: "))

y = int(input("Y: "))

print(x + y)