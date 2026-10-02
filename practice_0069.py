# Practicing Session:
name = input("Name: ")
number = input("Number: ")

print(f"Hello, {name}. Your number '{number}' has been saved.")

digit = int(input("Digit: "))

for i in range(1, digit + 1):
    print(' ' * (digit - i) + '#' * i, ' ','#' * i)