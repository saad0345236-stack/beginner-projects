# Printing 4 even numbers:
count_1 = 0
for digit in range(1, 10):
    if digit % 2 == 0:
        print(digit)
        count_1 += 1
print(f"We have {count_1} even numbers.")
# Printing 4 odd numbers:
count_2 = 0
for number in range(1, 10):
    if number % 2 != 0:
        print(number)
        count_2 += 1
print(f"We have {count_2} odd numbers.")
print(f"We now have {count_1} even numbers & {count_2} odd numbers.")