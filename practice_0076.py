# Practicing Session:
import time

phone_number = "012–345–6789"

for i in phone_number:
    if i == "–":
        continue
    print(i, end="")

print()

while True:
    for i in range(1, 16):
        if i == 10:
            pass
        else:
            print(i)

    name = input("Enter name: ")

    if name != "":
        break

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy new year!")

for i in "Germany":
    print(i)