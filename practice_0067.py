# Practicing Drill:
x = int(input('No 1: '))
y = int(input('No 2: '))

z = x / y

print(f"{z:.15f}")

if x < y:
    print(f"{x} is not greater than {y}.")
elif x > y:
    print(f"{x} is greater than {y}.")
else:
    print(f"{x} is equal to {y}.")

s = input()
t = input()

if s == t:
    print("Same")
else:
    print("Different")

answer = input("Do you agree? ").lower()

if answer in ['y', 'yes']:
    print("Agreed.")
else:
    print("Not agreed.")

name = input("Name: ")

capitalize = name.capitalize()

print(f"Name: {name}")
print(f"Capitalized: {capitalize}")

before = name

after = before.upper()

print(f"Before: {name}")
print(f"After: {after}")

def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("Meow")

main()